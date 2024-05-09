import csv


if __name__ == '__main__':

    octave_note_list: list[str] = [
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
    ]

    output_file = "defs/note_def.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["midi_value", "note"])
        for octave in range(11):
            for idx, note in enumerate(octave_note_list):
                midi_value = octave * 12 + idx
                if midi_value > 127:
                    break
                note_str = note + str(octave - 1) if len(note) == 1 else note[0] + str(octave - 1) + note[1]
                writer.writerow([midi_value, note_str])
