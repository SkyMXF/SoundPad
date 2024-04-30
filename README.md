# SoundPad

[中文版说明](https://github.com/SkyMXF/SoundPad/blob/main/README_CN.md)

### Requirements
If you dont have any available midi port on your PC, you need to create a virtual midi port.

[loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) is recommended to create virtual midi ports. you can also use other ways.

### Description
This tool can send MIDI signal by the touch (mouse click / graphics tablet). Other softwares (like Reaper) can accept the MIDI and do some predefined work.
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/midi_signal_pipe.png)

Six types of inputs can be converted to MIDI signals:
- Press Event: The left mouse button down event. This event can be connected to a MIDI signal that starts play audio or starts recording something.
- Release Event: The left mouse button up event. This event can be connected to a MIDI signal that stops play audio or stops recording something.
- X-Axis Position: When the left mouse button is down, the x-axis position of the mouse will be converted to a 0 to 127 value and send as the value of given MIDI CC.
- Y-Axis Position: The same to the X-Axis Position. These two info can be connected to MIDI signals that control the pan / volume / pitch or some other properties of the audio.
- Pressure: When you are using a graphics tablet to control the mouse, the pressure of the pen can also be connected to a MIDI CC value.
- Speed: When the left mouse button is down, the moving speed of your mouse can also be connected to a MIDI CC value.


### Reaper Control Example
Here is an example of how to use this tool to control Reaper. In this example, we will use the mouse position to control the pan and pitch of a track and record the audio to another track.

1. Install [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) and create a virtual MIDI port.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/loop_midi_usage.png)

2. Open SoundPad and set the MIDI port to the virtual MIDI port. Click Refresh if the port is not shown.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_port_in_sound_pad.png)

3. Open Reaper and activate the virtual MIDI port as a MIDI input device. (Options -> Preferences -> MIDI Devices)

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/enable_midi_in_reaper.png)

4. Create three tracks in reaper. The first track is for the audio source, the second track is for the MIDI input, and the third track is for recording.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/create_tracks.png)

5. Route the source track to the recording track. Route the MIDI input track to the source track. Drag the route line between the tracks or add "Send" in track routing can do this.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/route_1_to_3.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/route_2_to_1.png)

6. Open record of the MIDI input and recording track. Disable the record on MIDI input track (just monitoring). Set input of the MIDI input track to "Input: MIDI > loopMIDI Port". Set the record of the recording track to "Record: Output (Stereo)". Set the input of the recording track to "Input: None".

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_track_record.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_track_input.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_record_track_record.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_record_track_input.png)

7. Set MIDI CC 20 to start transport record and MICI CC 21 to stop transport (Actions -> Show action list -> search "record" -> add shortcut). Use "MIDI Send" module in SoundPad to send MIDI CC 20 or 21 to give Reaper a shortcut input.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/add_transport_control.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_midi.png)

8. Set MIDI CC 22 to control the pan of the first track (source track). (Actions -> Show action list -> search "pan" -> add shortcut)

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_pan.png)

9. Create a Pitch FX for the source track.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/add_pitch_fx.png)

10. In the Pitch FX, set the pitch to be controlled by MIDI CC 23.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_pitch.png)

11. Set every MIDI CC in SoundPad to the corresponding value.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_in_sound_pad.png)

12. Draw something on the SoundPad and the pan and pitch of the source track will change according to the position of the mouse.

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/control_effects.png)
