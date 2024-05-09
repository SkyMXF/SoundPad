import os
import math
from enum import Enum
from typing import Callable, Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PySide6.QtGui import QIcon, QMouseEvent, QCloseEvent, QPen, QColor

from ui.main_window.control_widgets.realtime_control_widget import Ui_realtime_control_widget
from utils.log import Logger
from utils.midi import CC_DEF, MIDI_CHANNELS, MIDI_VALUES, NOTE_DEF
from utils.config import UserConfig


class RealtimeMIDIType(Enum):
    NO_SEND = -1
    PITCH_WHEEL = 0
    CC = 1


class SensitivityType(Enum):
    RESTRICT = 0    # restrict the range
    FACTOR = 1      # use a factor to scale the range


class MIDITypeInfo(object):

    def __init__(self, midi_type: RealtimeMIDIType, value: any):
        self.midi_type = midi_type
        self.value = value


class RealtimeControlWidgetControl(QWidget, Ui_realtime_control_widget):

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        preset_cfg: UserConfig = None,
        preset_cfg_prefix: str = "",
        sensitive_range: tuple[float, float] = (0.5, 2.0),
        sensitive_type: SensitivityType = SensitivityType.RESTRICT,
    ):
        super(RealtimeControlWidgetControl, self).__init__(parent)
        self.setupUi(self)

        self.preset_cfg: UserConfig = preset_cfg
        self.preset_cfg_prefix: str = preset_cfg_prefix

        self.sensitive_range: tuple[float, float] = sensitive_range
        self.sensitive: float = 1.0
        self.sensitive_type: SensitivityType = sensitive_type
        self.realtime_midi_value_min_ratio: float = 0.0
        self.realtime_midi_value_max_ratio: float = 1.0

        self._init_midi_type_combo_box()
        self._init_channel_combo_box()
        self._init_slider_sens()

        # apply preset config
        self._load_cfg()

        self._connect_signals()

    # init midi type combo box
    def _init_midi_type_combo_box(self):
        self.combo_box_midi_type.clear()
        self.combo_box_midi_type.addItem("No Send", MIDITypeInfo(RealtimeMIDIType.NO_SEND, None))
        self.combo_box_midi_type.addItem("Pitch Wheel", MIDITypeInfo(RealtimeMIDIType.PITCH_WHEEL, None))
        for cc, desc in CC_DEF:
            self.combo_box_midi_type.addItem("CC %d: %s" % (cc, desc), MIDITypeInfo(RealtimeMIDIType.CC, cc))

    def _init_channel_combo_box(self):
        self.combo_box_channel.clear()
        for i in range(MIDI_CHANNELS):
            self.combo_box_channel.addItem(str(i + 1), i)

    def _init_slider_sens(self):
        self.slider_sens.setValue(
            int(((1.0 - self.sensitive_range[0]) / (self.sensitive_range[1] - self.sensitive_range[0])) * 10000) + 0.5
        )
        self._on_slider_sens_value_changed(self.slider_sens.value())

    def _connect_signals(self):
        self.slider_sens.valueChanged.connect(self._on_slider_sens_value_changed)

    def _on_slider_sens_value_changed(self, value: int):
        self.sensitive = value / 10000.0 * (self.sensitive_range[1] - self.sensitive_range[0]) + self.sensitive_range[0]
        self.label_sens.setText("%.2f" % self.sensitive)
        if self.sensitive_type == SensitivityType.RESTRICT:
            # update min and max range
            self.realtime_midi_value_min_ratio = 0.5 - 0.5 * self.sensitive
            self.realtime_midi_value_max_ratio = 0.5 + 0.5 * self.sensitive

    def _get_midi_value(self, realtime_ratio: float, base: int = 128):
        if self.sensitive_type == SensitivityType.RESTRICT:
            midi_value = realtime_ratio * (
                    self.realtime_midi_value_max_ratio - self.realtime_midi_value_min_ratio
            ) + self.realtime_midi_value_min_ratio
            midi_value = min(max(int(midi_value * base), 0), base - 1)
        elif self.sensitive_type == SensitivityType.FACTOR:
            midi_value = max(min(int(realtime_ratio * base * self.sensitive), base - 1), 0)
        else:
            Logger.error("Unknown sensitivity type: %s" % self.sensitive_type)
            midi_value = 0

        return midi_value

    # return: [status, data1, data2], midi_value
    def get_midi_msg(self, realtime_ratio: float) -> tuple[list[int], int] | None:
        midi_type_info: MIDITypeInfo = self.combo_box_midi_type.currentData()
        channel = self.combo_box_channel.currentData()

        if midi_type_info.midi_type == RealtimeMIDIType.NO_SEND:
            return None
        elif midi_type_info.midi_type == RealtimeMIDIType.PITCH_WHEEL:
            midi_value = self._get_midi_value(realtime_ratio, 16383)    # 14 bits
            return [0xE0 + channel, midi_value & 0x7F, (midi_value >> 7) & 0x7F], midi_value

        elif midi_type_info.midi_type == RealtimeMIDIType.CC:
            midi_value = self._get_midi_value(realtime_ratio, 128)
            return [0xB0 + channel, midi_type_info.value, midi_value], midi_value

    def _load_cfg(self):
        preset_midi_type_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_midi_type", 0)
        self.combo_box_midi_type.setCurrentIndex(preset_midi_type_idx)
        preset_channel_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_channel", 0)
        self.combo_box_channel.setCurrentIndex(preset_channel_idx)
        preset_sensitivity = self.preset_cfg.get_config(self.preset_cfg_prefix + "_sensitivity", self.slider_sens.value())
        self.slider_sens.setValue(preset_sensitivity)
        self._on_slider_sens_value_changed(preset_sensitivity)

    def save_cfg(self):
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_midi_type", self.combo_box_midi_type.currentIndex())
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_channel", self.combo_box_channel.currentIndex())
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_sensitivity", self.slider_sens.value())
