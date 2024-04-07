import os
import sys
import logging

from PySide6.QtWidgets import QApplication
from qt_material import build_stylesheet

from ui.main_window.main_window_control import MainWindowGUI
from utils.log import Logger, init_logger


def run_app_loop():
    app = QApplication([])

    main_window = MainWindowGUI(
        stylesheet=build_stylesheet(theme="dark_teal.xml", template="material.css"),
    )

    # set stylesheet
    app.setStyleSheet(main_window.stylesheet)

    # show window
    Logger.debug("Application started.")
    main_window.show()
    app_thread = app.exec()

    sys.exit(app_thread)


if __name__ == '__main__':

    init_logger(logging.DEBUG)

    try:
        run_app_loop()
    except Exception as e:
        Logger.exception(e)
