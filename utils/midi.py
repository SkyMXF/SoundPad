import os
import csv
import rtmidi
from typing import Optional

from utils.log import Logger


# load cc definition from csv file
CC_DEFINITION_PATH = os.path.join("defs", "cc_def.csv")
CC_DEF: list[tuple[int, str]] = []
if os.path.exists(CC_DEFINITION_PATH):
    with open(CC_DEFINITION_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if len(row) < 2:
                continue
            cc = int(row[0])
            desc = row[1]
            CC_DEF.append((cc, desc))

# load note definition from csv file
NOTE_DEFINITION_PATH = os.path.join("defs", "note_def.csv")
NOTE_DEF: list[tuple[int, str]] = []
if os.path.exists(NOTE_DEFINITION_PATH):
    with open(NOTE_DEFINITION_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if len(row) < 2:
                continue
            midi_value = int(row[0])
            note = row[1]
            NOTE_DEF.append((midi_value, note))

MIDI_CHANNELS = 16
MIDI_VALUES = 128


class MIDIConn(object):

    def __init__(self):
        self.out_stream: Optional[rtmidi.MidiOut] = None
        self.port_idx = -1

    @staticmethod
    def get_port_list() -> list[str]:
        out_stream = rtmidi.MidiOut()
        ports = out_stream.get_ports()
        del out_stream
        return ports

    def start(self, port_idx: int):
        self.out_stream = rtmidi.MidiOut()
        self.out_stream.open_port(port_idx)
        self.port_idx = port_idx

        Logger.info("MIDI port opened: %d" % port_idx)

    @property
    def is_available(self) -> bool:
        return self.out_stream is not None

    def send_midi_msg(self, value_list: list[int]):
        self.out_stream.send_message(value_list)

    def close(self):
        self.out_stream.delete()
        self.out_stream = None
        self.port_idx = -1

        Logger.info("MIDI port closed.")
