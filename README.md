# SoundPad

### Requirements
If you dont have any available midi port on your PC, you need to create a virtual midi port.

[loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) is recommended to create virtual midi ports. you can also use other ways.

### Description
This tool can send MIDI signal by the touch (mouse click / graphics tablet). Other softwares (like Reaper) can accept the MIDI and do some predefined work.

Six types of inputs can be converted to MIDI signals:
- Press Event: The left mouse button down event. This event can be connected to a MIDI signal that starts play audio or starts recording something.
- Release Event: The left mouse button up event. This event can be connected to a MIDI signal that stops play audio or stops recording something.
- X-Axis Position: When the left mouse button is down, the x-axis position of the mouse will be converted to a 0 to 127 value and send as the value of given MIDI CC.
- Y-Axis Position: The same to the X-Axis Position. These two info can be connected to MIDI signals that control the pan / volume / pitch or some other properties of the audio.
- Pressure: When you are using a graphics tablet to control the mouse, the pressure of the pen can also be connected to a MIDI CC value.
- Speed: When the left mouse button is down, the moving speed of your mouse can also be connected to a MIDI CC value.


### Reaper Control Example
