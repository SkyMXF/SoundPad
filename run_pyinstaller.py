import os
import shutil

import PyInstaller.__main__

if __name__ == '__main__':

    aim_dir = "release"
    res_files = [
        "cc_def.csv", "material.css"
    ]

    output_dir = os.path.join(".", "packaged")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    exe_name = "SoundPad"

    PyInstaller.__main__.run([
        # "--add-data=%s" % os.path.join(
        #    os.path.split(sys.executable)[0], "Lib", "site-packages", "qt_material"
        # ),
        "-F", "sound_pad.py",
        "-n", exe_name,
        "--specpath", os.path.join(output_dir, "spec"),
        "--distpath", os.path.join(output_dir, "dist"),
        "--workpath", os.path.join(output_dir, "build"),
        # "--noupx",
        # *hidden_import_params
    ])

    # 复制exe至根目录
    exe_src_path = os.path.join(output_dir, "dist", "%s.exe" % exe_name)
    exe_aim_path = os.path.join(aim_dir, "%s.exe" % exe_name)
    if not os.path.exists(aim_dir):
        os.makedirs(aim_dir)
    if os.path.exists(exe_aim_path):
        os.remove(exe_aim_path)
    shutil.copy(exe_src_path, exe_aim_path)
    for res_file in res_files:
        shutil.copy(res_file, os.path.join(aim_dir, res_file))
