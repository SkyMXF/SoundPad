import os
import math
from enum import Enum
from typing import Callable, Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PySide6.QtGui import QIcon, QMouseEvent, QCloseEvent, QPen, QColor

from ui.main_window.control_widgets.one_shot_control_widget import Ui_one_shot_control_widget
from utils.log import Logger
from utils.midi import CC_DEF, MIDI_CHANNELS, MIDI_VALUES, NOTE_DEF
from utils.config import UserConfig


class OneShotMIDIType(Enum):
    NO_SEND = -1
    NOTE = 0
    CC = 1


class MIDITypeInfo(object):

    def __init__(self, midi_type: OneShotMIDIType, value: any):
        self.midi_type = midi_type
        self.value = value


class OneShotControlWidgetControl(QWidget, Ui_one_shot_control_widget):

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        preset_cfg: UserConfig = None,
        preset_cfg_prefix: str = "",
    ):
        super(OneShotControlWidgetControl, self).__init__(parent)
        self.setupUi(self)

        self.preset_cfg: UserConfig = preset_cfg
        self.preset_cfg_prefix: str = preset_cfg_prefix

        self._init_midi_type_combo_box()
        self._init_channel_combo_box()

        # apply preset config
        self._load_cfg()

        self._connect_signals()

    # init midi type combo box
    def _init_midi_type_combo_box(self):
        self.combo_box_midi_type.clear()
        self.combo_box_midi_type.addItem("No Send", MIDITypeInfo(OneShotMIDIType.NO_SEND, None))
        self.combo_box_midi_type.addItem("Note On", MIDITypeInfo(OneShotMIDIType.NOTE, True))
        self.combo_box_midi_type.addItem("Note Off", MIDITypeInfo(OneShotMIDIType.NOTE, False))
        for cc, desc in CC_DEF:
            self.combo_box_midi_type.addItem("CC %d: %s" % (cc, desc), MIDITypeInfo(OneShotMIDIType.CC, cc))

    def _init_channel_combo_box(self):
        self.combo_box_channel.clear()
        for i in range(MIDI_CHANNELS):
            self.combo_box_channel.addItem(str(i + 1), i)

    def _connect_signals(self):
        self.combo_box_midi_type.currentIndexChanged.connect(self._on_midi_type_combo_box_changed)

    # set value label and combo box by selected midi type
    def _on_midi_type_combo_box_changed(self):
        midi_type_info: MIDITypeInfo = self.combo_box_midi_type.currentData()
        if midi_type_info.midi_type == OneShotMIDIType.NO_SEND:
            # no value
            self.combo_box_value_1.clear()
            self.combo_box_value_1.setDisabled(True)

            self.combo_box_value_2.clear()
            self.combo_box_value_2.setDisabled(True)
        elif midi_type_info.midi_type == OneShotMIDIType.NOTE:
            # note in value 1
            self.combo_box_value_1.clear()
            self.combo_box_value_1.setEnabled(True)
            for note, desc in NOTE_DEF:
                self.combo_box_value_1.addItem("%d: %s" % (note, desc), note)

            # velocity in value 2
            self.combo_box_value_2.clear()
            self.combo_box_value_2.setEnabled(True)
            for i in range(MIDI_VALUES):
                self.combo_box_value_2.addItem("Velocity: %d" % i, i)
        elif midi_type_info.midi_type == OneShotMIDIType.CC:
            # cc value in value 1
            self.combo_box_value_1.clear()
            self.combo_box_value_1.setEnabled(True)
            for i in range(MIDI_VALUES):
                self.combo_box_value_1.addItem("Value: %d" % i, i)

            # no value 2
            self.combo_box_value_2.clear()
            self.combo_box_value_2.setDisabled(True)

    def get_midi_msg(self) -> list[int] | None:
        midi_type_info: MIDITypeInfo = self.combo_box_midi_type.currentData()
        channel = self.combo_box_channel.currentData()
        value_1 = self.combo_box_value_1.currentData()
        value_2 = self.combo_box_value_2.currentData()

        if midi_type_info.midi_type == OneShotMIDIType.NO_SEND:
            return None
        elif midi_type_info.midi_type == OneShotMIDIType.NOTE:
            # midi_type_info.value is True for Note On, False for Note Off
            if midi_type_info.value:
                return [0x90 + channel, value_1, value_2]
            else:
                return [0x80 + channel, value_1, value_2]
        elif midi_type_info.midi_type == OneShotMIDIType.CC:
            return [0xB0 + channel, midi_type_info.value, value_1]

    def _load_cfg(self):
        preset_midi_type_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_midi_type", 0)
        self.combo_box_midi_type.setCurrentIndex(preset_midi_type_idx)
        self._on_midi_type_combo_box_changed()

        preset_channel_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_channel", 0)
        self.combo_box_channel.setCurrentIndex(preset_channel_idx)

        preset_value_1_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_value_1", 0)
        self.combo_box_value_1.setCurrentIndex(preset_value_1_idx)

        preset_value_2_idx = self.preset_cfg.get_config(self.preset_cfg_prefix + "_value_2", 0)
        self.combo_box_value_2.setCurrentIndex(preset_value_2_idx)

    def save_cfg(self):
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_midi_type", self.combo_box_midi_type.currentIndex())
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_channel", self.combo_box_channel.currentIndex())
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_value_1", self.combo_box_value_1.currentIndex())
        self.preset_cfg.set_config(self.preset_cfg_prefix + "_value_2", self.combo_box_value_2.currentIndex())
