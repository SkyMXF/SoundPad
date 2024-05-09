import os
import math
from typing import Callable, Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PySide6.QtGui import QIcon, QMouseEvent, QCloseEvent, QPen, QColor

from ui.main_window.main_window import Ui_main_window_sound_pad
from ui.main_window.control_widgets.realtime_control_widget_control import RealtimeControlWidgetControl, SensitivityType
from ui.main_window.control_widgets.one_shot_control_widget_control import OneShotControlWidgetControl
from utils.log import Logger
from utils.midi import CC_DEF, MIDI_CHANNELS, MIDI_VALUES, MIDIConn
from utils.config import UserConfig


MOVE_SPEED_ATTACK_TIME = 0.1
MOVE_SPEED_RELEASE_TIME = 0.1
MOUSE_CHECK_FPS = 50
PEN_COLOR = QColor(255, 255, 255)
PEN_THICKNESS = 2


class MainWindowGUI(QMainWindow, Ui_main_window_sound_pad):

    def __init__(self, stylesheet: str | None = None):
        super(MainWindowGUI, self).__init__()
        self.setupUi(self)

        self.stylesheet = stylesheet

        # control panel variables
        self.is_mouse_down = False
        self.x_axis_ratio: float = 0.0
        self.x_axis_sensitive_range: tuple[float, float] = (0.5, 2.0)
        self.y_axis_ratio: float = 0.0
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

        # pos check
        self.pos_cache: tuple[int, int] = (0, 0)
        self.last_pos_cache: tuple[int, int] | None = None
        self.pos_update_timer = QTimer(self)
        self.pos_update_timer.timeout.connect(self.on_update_pos)
        self.pos_update_timer.start(1000 // MOUSE_CHECK_FPS)

        # midi signal setting widgets
        self.x_axis_midi_set_widget = RealtimeControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="x_axis",
            sensitive_range=(0.5, 2.0), sensitive_type=SensitivityType.RESTRICT)
        self.y_axis_midi_set_widget = RealtimeControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="y_axis",
            sensitive_range=(0.5, 2.0), sensitive_type=SensitivityType.RESTRICT)
        self.speed_midi_set_widget = RealtimeControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="speed",
            sensitive_range=(0.125, 8.0), sensitive_type=SensitivityType.FACTOR)
        self.pressure_midi_set_widget = RealtimeControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="pressure",
            sensitive_range=(0.125, 8.0), sensitive_type=SensitivityType.FACTOR)
        self.press_midi_set_widget = OneShotControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="press")
        self.release_midi_set_widget = OneShotControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="release")
        self.midi_send_midi_set_widget = OneShotControlWidgetControl(
            parent=self, preset_cfg=UserConfig(), preset_cfg_prefix="midi_send")

        # midi signal uis
        self.init_midi_signal_ui()

        # status bar
        self.status_label_x_axis: Optional[QLabel] = None
        self.status_label_y_axis: Optional[QLabel] = None
        self.status_label_speed: Optional[QLabel] = None
        self.status_label_pressure: Optional[QLabel] = None
        self.init_status_bar()

        # set control panel
        self.pen = QPen(PEN_COLOR, PEN_THICKNESS)
        self.graphics_scene = QGraphicsScene(self)
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

        self.vertical_layout_x_axis_group.addWidget(self.x_axis_midi_set_widget)
        self.vertical_layout_y_axis_group.addWidget(self.y_axis_midi_set_widget)
        self.vertical_layout_speed_group.addWidget(self.speed_midi_set_widget)
        self.vertical_layout_pressure_group.addWidget(self.pressure_midi_set_widget)
        self.vertical_layout_press_event_group.addWidget(self.press_midi_set_widget)
        self.vertical_layout_release_event_group.addWidget(self.release_midi_set_widget)
        self.horizontal_layout_midi_send_group.insertWidget(0, self.midi_send_midi_set_widget)

    def save_midi_signal_config(self):
        cfg = UserConfig()
        cfg.set_config("midi_port", self.combo_box_midi_port.currentIndex())
        self.x_axis_midi_set_widget.save_cfg()
        self.y_axis_midi_set_widget.save_cfg()
        self.speed_midi_set_widget.save_cfg()
        self.pressure_midi_set_widget.save_cfg()
        self.press_midi_set_widget.save_cfg()
        self.release_midi_set_widget.save_cfg()
        self.midi_send_midi_set_widget.save_cfg()

    def load_midi_signal_config(self):
        cfg = UserConfig()
        self.combo_box_midi_port.setCurrentIndex(cfg.get_config("midi_port", 0))

    def on_click_midi_send(self):
        self.midi_conn.send_midi_msg(
            self.midi_send_midi_set_widget.get_midi_msg()
        )

    # endregion

    # region control panel

    def init_control_panel(self):
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.resizeEvent = self.on_panel_resize
        self.graphics_view.mousePressEvent = self.on_panel_mouse_down
        self.graphics_view.mouseReleaseEvent = self.on_panel_mouse_up
        self.graphics_view.tabletEvent = self.on_panel_tablet_event

    def on_panel_resize(self, event):
        self.graphics_scene.setSceneRect(0, 0, self.graphics_view.width(), self.graphics_view.height())

    def on_panel_mouse_down(self, event: QMouseEvent):
        self.clear_graphics()
        self.is_mouse_down = True
        midi_msg = self.press_midi_set_widget.get_midi_msg()
        if midi_msg is not None:
            self.midi_conn.send_midi_msg(midi_msg)

    def on_panel_mouse_up(self, event: QMouseEvent):
        self.is_mouse_down = False
        midi_msg = self.release_midi_set_widget.get_midi_msg()
        if midi_msg is not None:
            self.midi_conn.send_midi_msg(midi_msg)

    def on_panel_tablet_event(self, event):
        self.pressure = event.pressure()

    def draw_line(self, x1: float, y1: float, x2: float, y2: float):
        self.graphics_scene.addLine(x1, y1, x2, y2, self.pen)

    def clear_graphics(self):
        self.graphics_scene.clear()

    def on_update_pos(self):
        cursor = self.graphics_view.mapFromGlobal(self.cursor().pos())
        self.pos_cache = (cursor.x(), cursor.y())
        self.x_axis_ratio = self.pos_cache[0] / self.graphics_view.width()
        self.y_axis_ratio = self.pos_cache[1] / self.graphics_view.height()
        self.y_axis_ratio = 1.0 - self.y_axis_ratio     # reverse y axis

        # xy position
        x_msg_tuple = self.x_axis_midi_set_widget.get_midi_msg(self.x_axis_ratio)
        if x_msg_tuple is not None:
            x_midi_msg, x_midi_value = self.x_axis_midi_set_widget.get_midi_msg(self.x_axis_ratio)
        else:
            x_midi_msg, x_midi_value = None, 0
        y_msg_tuple = self.y_axis_midi_set_widget.get_midi_msg(self.y_axis_ratio)
        if y_msg_tuple is not None:
            y_midi_msg, y_midi_value = self.y_axis_midi_set_widget.get_midi_msg(self.y_axis_ratio)
        else:
            y_midi_msg, y_midi_value = None, 0
        self.update_status_bar_axis(x_midi_value, y_midi_value)

        # mouse move speed
        x_delta = self.x_axis_ratio - self.move_speed_last_x
        y_delta = self.y_axis_ratio - self.move_speed_last_y
        time_delta = self.pos_update_timer.interval() / 1000.0
        self.move_speed = min(
            (x_delta * x_delta + y_delta * y_delta) / (time_delta * time_delta) / self.move_speed_base_value, 1.0)
        smooth_time = MOVE_SPEED_ATTACK_TIME if self.move_speed > self.smooth_move_speed else MOVE_SPEED_RELEASE_TIME
        self.smooth_move_speed = (self.smooth_move_speed
                                  + (self.move_speed - self.smooth_move_speed) * time_delta / smooth_time)
        speed_msg_tuple = self.speed_midi_set_widget.get_midi_msg(self.smooth_move_speed)
        self.move_speed_last_x = self.x_axis_ratio
        self.move_speed_last_y = self.y_axis_ratio
        self.update_status_bar_speed(speed_msg_tuple[1] if speed_msg_tuple is not None else 0)

        # pressure
        pressure_msg_tuple = self.pressure_midi_set_widget.get_midi_msg(self.pressure)
        self.update_status_bar_pressure(pressure_msg_tuple[1] if pressure_msg_tuple is not None else 0)

        if self.is_mouse_down:
            if self.last_pos_cache is not None:
                self.draw_line(
                    self.last_pos_cache[0], self.last_pos_cache[1],
                    self.pos_cache[0], self.pos_cache[1])
            self.last_pos_cache = self.pos_cache
            if x_midi_msg is not None:
                self.midi_conn.send_midi_msg(x_midi_msg)
            if y_midi_msg is not None:
                self.midi_conn.send_midi_msg(y_midi_msg)
            if speed_msg_tuple is not None:
                self.midi_conn.send_midi_msg(speed_msg_tuple[0])
            if pressure_msg_tuple is not None:
                self.midi_conn.send_midi_msg(pressure_msg_tuple[0])
        else:
            self.last_pos_cache = None

    # endregion

    # region midi connection

    def init_midi_ports_view(self):
        self.on_refresh_midi_ports()
        self.push_button_refresh_midi_port.clicked.connect(self.on_refresh_midi_ports)
        self.on_select_midi_port()
        self.combo_box_midi_port.currentIndexChanged.connect(self.on_select_midi_port)
        self.push_button_send_midi.clicked.connect(self.on_click_midi_send)

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
