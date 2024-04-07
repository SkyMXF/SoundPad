import os
import math
from typing import Callable, Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QLabel
from PySide6.QtGui import QIcon, QMouseEvent, QCloseEvent

from ui.main_window.main_window import Ui_main_window_sound_pad
from utils.log import Logger
from utils.midi import CC_DEF, MIDI_CHANNELS, MIDI_VALUES, MIDIConn
from utils.config import UserConfig


MOVE_SPEED_ATTACK_TIME = 0.1
MOVE_SPEED_RELEASE_TIME = 0.1
MOUSE_CHECK_FPS = 50


class MainWindowGUI(QMainWindow, Ui_main_window_sound_pad):

    def __init__(self, stylesheet: str | None = None):
        super(MainWindowGUI, self).__init__()
        self.setupUi(self)

        self.stylesheet = stylesheet

        # control panel variables
        self.is_mouse_down = False
        self.x_axis_ratio: float = 0.0
        self.x_axis_midi_value_min: int = 0
        self.x_axis_midi_value_max: int = 128
        self.x_axis_sensitive_range: tuple[float, float] = (0.5, 2.0)
        self.y_axis_ratio: float = 0.0
        self.y_axis_midi_value_min: int = 0
        self.y_axis_midi_value_max: int = 128
        self.y_axis_sensitive_range: tuple[float, float] = (0.5, 2.0)
        self.move_speed: float = 0.0
        self.smooth_move_speed: float = 0.0
        self.move_speed_base_value: float = 9.0         # squared value, 3 screen size per second as max speed
        self.move_speed_last_x: float = 0.0
        self.move_speed_last_y: float = 0.0
        self.move_speed_sensitive: float = 1.0
        self.move_speed_sensitive_range: tuple[float, float] = (0.125, 8.0)
        self.pressure: float = 0.0
        self.pressure_sensitive: float = 1.0
        self.pressure_sensitive_range: tuple[float, float] = (0.125, 8.0)

        # mouse check timer
        self.mouse_check_timer = QTimer(self)
        self.mouse_check_timer.timeout.connect(self.on_check_mouse_pos)
        self.mouse_check_timer.start(1000 // MOUSE_CHECK_FPS)

        # midi signal uis
        self.midi_combo_box_cfg_binds = {
            "x_axis_midi_cc": self.combo_box_midi_cc_x_axis,
            "x_axis_midi_chn": self.combo_box_chn_x_axis,
            "y_axis_midi_cc": self.combo_box_midi_cc_y_axis,
            "y_axis_midi_chn": self.combo_box_chn_y_axis,
            "speed_midi_cc": self.combo_box_midi_cc_speed,
            "speed_midi_chn": self.combo_box_chn_speed,
            "pressure_midi_cc": self.combo_box_midi_cc_pressure,
            "pressure_midi_chn": self.combo_box_chn_pressure,
            "press_midi_cc": self.combo_box_midi_cc_press,
            "press_midi_chn": self.combo_box_chn_press,
            "press_midi_value": self.combo_box_value_press,
            "release_midi_cc": self.combo_box_midi_cc_release,
            "release_midi_chn": self.combo_box_chn_release,
            "release_midi_value": self.combo_box_value_release,
            "midi_port": self.combo_box_midi_port,
        }
        self.midi_slider_cfg_binds = {
            "x_axis_sens": self.slider_sens_x_axis,
            "y_axis_sens": self.slider_sens_y_axis,
            "speed_sens": self.slider_sens_speed,
            "pressure_sens": self.slider_sens_pressure,
        }
        self.init_midi_signal_ui()

        # midi signal controls
        self.init_midi_signal_controls()

        # status bar
        self.status_label_x_axis: Optional[QLabel] = None
        self.status_label_y_axis: Optional[QLabel] = None
        self.status_label_speed: Optional[QLabel] = None
        self.status_label_pressure: Optional[QLabel] = None
        self.init_status_bar()

        # set control panel
        self.init_control_panel()

        # midi connection
        self.midi_conn: MIDIConn = MIDIConn()
        self.init_midi_ports_view()

        # setting from user config
        self.load_midi_signal_config()

    # region status bar

    def init_status_bar(self):
        self.status_label_x_axis = QLabel()
        self.status_label_y_axis = QLabel()
        self.status_label_speed = QLabel()
        self.status_label_pressure = QLabel()
        self.statusBar.addPermanentWidget(self.status_label_x_axis)
        self.statusBar.addPermanentWidget(self.status_label_y_axis)
        self.statusBar.addPermanentWidget(self.status_label_speed)
        self.statusBar.addPermanentWidget(self.status_label_pressure)

    def update_status_bar_axis(self, x_value: int, y_value: int):
        self.status_label_x_axis.setText("X-axis MIDI value: %d" % x_value)
        self.status_label_y_axis.setText("Y-axis MIDI value: %d" % y_value)

    def update_status_bar_speed(self, value: int):
        self.status_label_speed.setText("Speed MIDI value: %d" % value)

    def update_status_bar_pressure(self, value: int):
        self.status_label_pressure.setText("Pressure MIDI value: %d" % value)

    # endregion

    # region midi signals ui

    def init_midi_signal_ui(self):

        # midi cc definition combo boxes
        for combo_box in [
            self.combo_box_midi_cc_x_axis, self.combo_box_midi_cc_y_axis,
            self.combo_box_midi_cc_speed, self.combo_box_midi_cc_pressure,
            self.combo_box_midi_cc_press, self.combo_box_midi_cc_release
        ]:
            for cc, desc in CC_DEF:
                combo_box.addItem("%d: %s" % (cc, desc), cc)

        # midi channel combo boxes
        for combo_box in [
            self.combo_box_chn_x_axis, self.combo_box_chn_y_axis,
            self.combo_box_chn_speed, self.combo_box_chn_pressure,
            self.combo_box_chn_press, self.combo_box_chn_release
        ]:
            for i in range(MIDI_CHANNELS):
                combo_box.addItem("%d" % (i + 1), i)

        # midi values
        for combo_box in [
            self.combo_box_value_press, self.combo_box_value_release
        ]:
            for i in range(MIDI_VALUES):
                combo_box.addItem("%d" % i, i)

    def save_midi_signal_config(self):
        cfg = UserConfig()
        for key, combo_box in self.midi_combo_box_cfg_binds.items():
            cfg.set_config(key, combo_box.currentIndex())

        for key, slider in self.midi_slider_cfg_binds.items():
            cfg.set_config(key, slider.value())

    def load_midi_signal_config(self):
        cfg = UserConfig()
        for key, combo_box in self.midi_combo_box_cfg_binds.items():
            idx = cfg.get_config(key, default_value=combo_box.currentIndex())
            if idx < combo_box.count():
                combo_box.setCurrentIndex(idx)

        for key, slider in self.midi_slider_cfg_binds.items():
            value = cfg.get_config(key, default_value=slider.value())
            slider.setValue(max(min(value, slider.maximum()), slider.minimum()))

    # endregion

    # region midi signals send

    def init_midi_signal_controls(self):
        self.slider_sens_x_axis.valueChanged.connect(self.on_x_axis_sens_slider_change)
        self.slider_sens_y_axis.valueChanged.connect(self.on_y_axis_sens_slider_change)
        self.slider_sens_speed.valueChanged.connect(self.on_speed_sens_slider_change)
        self.slider_sens_pressure.valueChanged.connect(self.on_pressure_sens_slider_change)

        self.slider_sens_x_axis.setValue(
            int(((1.0 - self.x_axis_sensitive_range[0]) / (self.x_axis_sensitive_range[1] - self.x_axis_sensitive_range[0])) * 10000) + 0.5)
        self.slider_sens_y_axis.setValue(
            int(((1.0 - self.y_axis_sensitive_range[0]) / (self.y_axis_sensitive_range[1] - self.y_axis_sensitive_range[0])) * 10000) + 0.5)
        self.slider_sens_speed.setValue(
            int((self.move_speed_sensitive - self.move_speed_sensitive_range[0]) / (self.move_speed_sensitive_range[1] - self.move_speed_sensitive_range[0]) * 10000) + 0.5)
        self.slider_sens_pressure.setValue(
            int((self.pressure_sensitive - self.pressure_sensitive_range[0]) / (self.pressure_sensitive_range[1] - self.pressure_sensitive_range[0]) * 10000) + 0.5)

    def on_x_axis_sens_slider_change(self, value: int):
        sensitive = value / 10000.0 * (
            self.x_axis_sensitive_range[1] - self.x_axis_sensitive_range[0]) + self.x_axis_sensitive_range[0]
        self.label_x_axis_sens.setText("%.3f" % sensitive)
        self.x_axis_midi_value_min = int(64 - 64 * sensitive)
        self.x_axis_midi_value_max = int(64 + 64 * sensitive)

    def on_y_axis_sens_slider_change(self, value: int):
        sensitive = value / 10000.0 * (
            self.y_axis_sensitive_range[1] - self.y_axis_sensitive_range[0]) + self.y_axis_sensitive_range[0]
        self.label_y_axis_sens.setText("%.3f" % sensitive)
        self.y_axis_midi_value_min = int(64 - 64 * sensitive)
        self.y_axis_midi_value_max = int(64 + 64 * sensitive)

    def on_speed_sens_slider_change(self, value: int):
        self.move_speed_sensitive = value / 10000.0 * (
            self.move_speed_sensitive_range[1] - self.move_speed_sensitive_range[0]) + self.move_speed_sensitive_range[0]
        self.label_speed_sens.setText("%.3f" % self.move_speed_sensitive)

    def on_pressure_sens_slider_change(self, value: int):
        self.pressure_sensitive = value / 10000.0 * (
            self.pressure_sensitive_range[1] - self.pressure_sensitive_range[0]) + self.pressure_sensitive_range[0]
        self.label_pressure_sens.setText("%.3f" % self.pressure_sensitive)

    @property
    def x_axis_midi_value(self) -> int:
        return min(
            max(
                int(
                    self.x_axis_ratio * (self.x_axis_midi_value_max - self.x_axis_midi_value_min)
                ) + self.x_axis_midi_value_min,
                0),
            127)

    @property
    def y_axis_midi_value(self) -> int:
        return min(
            max(
                int(
                    self.y_axis_ratio * (self.y_axis_midi_value_max - self.y_axis_midi_value_min)
                ) + self.y_axis_midi_value_min,
                0),
            127)

    @property
    def move_speed_midi_value(self) -> int:
        return max(min(int(self.smooth_move_speed * self.move_speed_sensitive * 128), 127), 0)

    @property
    def pressure_midi_value(self) -> int:
        return max(min(int(self.pressure * self.pressure_sensitive * 128), 127), 0)

    # endregion

    # region control panel

    def init_control_panel(self):
        self.frame_control_panel.setStyleSheet("background-color: black;")
        self.frame_control_panel.mousePressEvent = self.on_panel_mouse_down
        self.frame_control_panel.mouseReleaseEvent = self.on_panel_mouse_up

    def on_panel_mouse_down(self, event: QMouseEvent):
        self.is_mouse_down = True
        self.midi_conn.send_midi_msg(
            self.combo_box_midi_cc_press.currentData(),
            self.combo_box_chn_press.currentData(),
            self.combo_box_value_press.currentData())

    def on_panel_mouse_up(self, event: QMouseEvent):
        self.is_mouse_down = False
        self.midi_conn.send_midi_msg(
            self.combo_box_midi_cc_release.currentData(),
            self.combo_box_chn_release.currentData(),
            self.combo_box_value_release.currentData())

    def on_check_mouse_pos(self):
        # xy position
        cursor = self.frame_control_panel.mapFromGlobal(self.cursor().pos())
        self.x_axis_ratio = cursor.x() / self.frame_control_panel.width()
        self.y_axis_ratio = cursor.y() / self.frame_control_panel.height()
        x_midi_value = self.x_axis_midi_value
        y_midi_value = self.y_axis_midi_value
        self.update_status_bar_axis(x_midi_value, y_midi_value)

        # mouse move speed
        x_delta = self.x_axis_ratio - self.move_speed_last_x
        y_delta = self.y_axis_ratio - self.move_speed_last_y
        time_delta = self.mouse_check_timer.interval() / 1000.0
        self.move_speed = min(
            (x_delta * x_delta + y_delta * y_delta) / (time_delta * time_delta) / self.move_speed_base_value, 1.0)
        smooth_time = MOVE_SPEED_ATTACK_TIME if self.move_speed > self.smooth_move_speed else MOVE_SPEED_RELEASE_TIME
        self.smooth_move_speed = (self.smooth_move_speed
                                  + (self.move_speed - self.smooth_move_speed) * time_delta / smooth_time)
        move_speed_midi_value = self.move_speed_midi_value
        self.move_speed_last_x = self.x_axis_ratio
        self.move_speed_last_y = self.y_axis_ratio
        self.update_status_bar_speed(move_speed_midi_value)

        if self.is_mouse_down:
            self.midi_conn.send_midi_msg(
                self.combo_box_midi_cc_x_axis.currentData(),
                self.combo_box_chn_x_axis.currentData(),
                x_midi_value)
            self.midi_conn.send_midi_msg(
                self.combo_box_midi_cc_y_axis.currentData(),
                self.combo_box_chn_y_axis.currentData(),
                y_midi_value)
            self.midi_conn.send_midi_msg(
                self.combo_box_midi_cc_speed.currentData(),
                self.combo_box_chn_speed.currentData(),
                move_speed_midi_value)

    # endregion

    # region midi connection

    def init_midi_ports_view(self):
        self.on_refresh_midi_ports()
        self.push_button_refresh_midi_port.clicked.connect(self.on_refresh_midi_ports)
        self.on_select_midi_port()
        self.combo_box_midi_port.currentIndexChanged.connect(self.on_select_midi_port)

    def on_refresh_midi_ports(self):
        self.combo_box_midi_port.clear()
        for port in MIDIConn.get_port_list():
            self.combo_box_midi_port.addItem(port)

    def on_select_midi_port(self):
        port_idx = self.combo_box_midi_port.currentIndex()
        if self.midi_conn.is_available:
            if self.midi_conn.port_idx == port_idx:
                return
            self.midi_conn.close()
        self.midi_conn.start(port_idx)

    # endregion

    # save config on close
    def closeEvent(self, event: QCloseEvent):
        self.save_midi_signal_config()
        event.accept()
