# SoundPad

### Demo Video
[Bilibili](https://www.bilibili.com/video/BV1KD421M76i/?share_source=copy_web&vd_source=5c7681b720da88e0cbbd8ec41a82594d)

https://github.com/SkyMXF/SoundPad/assets/30136123/ae0cf3b1-cb3f-4909-a9da-61e4fc5d606f

### 使用前
使用前，需要使用一些其他软件创建虚拟MIDI端口。

推荐使用 [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) 来创建。也可以使用其他有同类功能的软件。

### 功能说明
该工具能够将手势（通过鼠标或数位板控制）转化为指定的MIDI信号。可以在其他软件（如Reaper）中收到这些MIDI信号，并执行设定的行为。
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/midi_signal_pipe_cn.png)

SoundPad能够将六种手势输入形式转换为MIDI信号：
- 按下：鼠标左键按下事件。可以将该事件连接到一个MIDI信号，例如用于开始播放音频或开始录制音频。
- 弹起：鼠标左键弹起事件。可以将该事件连接到一个MIDI信号，例如用于停止播放音频或停止录制音频。
- X轴位置：当鼠标左键按下时，鼠标在SoundPad控制区的X轴位置将被转换为0到127的值，并作为给定MIDI CC的值发送。
- Y轴位置：与X轴位置相同。这两个信息可以连接到控制音频的平移/音量/音调或其他属性的MIDI信号。
- 压力：当使用数位板控制鼠标时，笔的压力也可以连接到MIDI CC值。
- 速度：当鼠标左键按下时，鼠标的移动速度也可以连接到MIDI CC值。

### 一个Reaper控制的例子
接下来是一个使用SoundPad控制Reaper的例子。在这个例子中，将使用鼠标位置来控制一条音轨的声相和音调，并将变化后的音频录制到另一条音轨中。

1. 安装 [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) 并创建一个虚拟MIDI端口。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/loop_midi_usage.png)

2. 打开SoundPad并将MIDI端口设置为虚拟MIDI端口。如果端口没有显示，尝试点击Refresh。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_port_in_sound_pad.png)

3. 打开Reaper并启用虚拟MIDI端口作为MIDI输入设备。（选项 -> 首选项 -> MIDI设备）

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/enable_midi_in_reaper.png)

4. 在Reaper中创建三条音轨。第一条音轨用于放置源素材，第二条音轨用于MIDI输入，第三条音轨用于录音。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/create_tracks.png)

5. 将源音轨Route到录音音轨。将MIDI输入音轨Route到源音轨。可以通过拖动音轨之间的Route按钮或在音轨路由中添加“Send”来实现。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/route_1_to_3.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/route_2_to_1.png)

6. 打开MIDI输入音轨和录音音轨的录音功能。禁用MIDI输入音轨的录音（仅监控）。将MIDI输入音轨的输入设置为“Input: MIDI > loopMIDI Port”。将录音音轨的录音设置为“Record: Output (Stereo)”。将录音音轨的输入设置为“Input: None”。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_track_record.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_midi_track_input.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_record_track_record.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_record_track_input.png)

7. 将MIDI CC 20设置为开始录音快捷键，将MIDI CC 21设置为停止录音快捷键（Actions -> Show action list -> search "record" -> add shortcut）。设置shortcut时，Reaper需要一个MIDI输入，使用SoundPad中的“MIDI Send”模块发送MIDI CC 20或21即可。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/add_transport_control.png)
![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_midi.png)

8. 将MIDI CC 22设置为控制第一条音轨（源音轨）的声相。（Actions -> Show action list -> search "pan" -> add shortcut）

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_pan.png)

9. 为源音轨创建一个Pitch FX。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/add_pitch_fx.png)

10. 在Pitch FX中，设置音调由MIDI CC 23控制。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/bind_pitch.png)

11. 在SoundPad中设置每个事件对应的MIDI CC。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/set_in_sound_pad.png)

12. 在SoundPad上做出一些手势，源音轨的声相和音调将根据鼠标的位置而变化。

![](https://raw.githubusercontent.com/SkyMXF/SoundPad/main/desc_img/control_effects.png)
