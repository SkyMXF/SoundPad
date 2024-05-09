# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_main_window_sound_pad(object):
    def setupUi(self, main_window_sound_pad):
        if not main_window_sound_pad.objectName():
            main_window_sound_pad.setObjectName(u"main_window_sound_pad")
        main_window_sound_pad.resize(1600, 900)
        self.centralwidget = QWidget(main_window_sound_pad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphics_view = QGraphicsView(self.centralwidget)
        self.graphics_view.setObjectName(u"graphics_view")
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphics_view.setForegroundBrush(brush)

        self.verticalLayout.addWidget(self.graphics_view)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.vertical_layout_x_axis_group = QVBoxLayout(self.groupBox)
        self.vertical_layout_x_axis_group.setObjectName(u"vertical_layout_x_axis_group")

        self.horizontalLayout_11.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.vertical_layout_y_axis_group = QVBoxLayout(self.groupBox_2)
        self.vertical_layout_y_axis_group.setObjectName(u"vertical_layout_y_axis_group")

        self.horizontalLayout_11.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.vertical_layout_speed_group = QVBoxLayout(self.groupBox_3)
        self.vertical_layout_speed_group.setObjectName(u"vertical_layout_speed_group")

        self.horizontalLayout_11.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.vertical_layout_pressure_group = QVBoxLayout(self.groupBox_4)
        self.vertical_layout_pressure_group.setObjectName(u"vertical_layout_pressure_group")

        self.horizontalLayout_11.addWidget(self.groupBox_4)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.vertical_layout_press_event_group = QVBoxLayout(self.groupBox_7)
        self.vertical_layout_press_event_group.setObjectName(u"vertical_layout_press_event_group")

        self.horizontalLayout_14.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFlat(False)
        self.vertical_layout_release_event_group = QVBoxLayout(self.groupBox_6)
        self.vertical_layout_release_event_group.setObjectName(u"vertical_layout_release_event_group")

        self.horizontalLayout_14.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontal_layout_midi_send_group = QHBoxLayout(self.groupBox_8)
        self.horizontal_layout_midi_send_group.setObjectName(u"horizontal_layout_midi_send_group")
        self.push_button_send_midi = QPushButton(self.groupBox_8)
        self.push_button_send_midi.setObjectName(u"push_button_send_midi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.push_button_send_midi.sizePolicy().hasHeightForWidth())
        self.push_button_send_midi.setSizePolicy(sizePolicy1)
        self.push_button_send_midi.setMaximumSize(QSize(70, 16777215))

        self.horizontal_layout_midi_send_group.addWidget(self.push_button_send_midi)


        self.horizontalLayout_14.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setMinimumSize(QSize(350, 0))
        self.groupBox_5.setMaximumSize(QSize(350, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.combo_box_midi_port = QComboBox(self.groupBox_5)
        self.combo_box_midi_port.setObjectName(u"combo_box_midi_port")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.combo_box_midi_port.sizePolicy().hasHeightForWidth())
        self.combo_box_midi_port.setSizePolicy(sizePolicy4)

        self.horizontalLayout_16.addWidget(self.combo_box_midi_port)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)

        self.push_button_refresh_midi_port = QPushButton(self.groupBox_5)
        self.push_button_refresh_midi_port.setObjectName(u"push_button_refresh_midi_port")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.push_button_refresh_midi_port.sizePolicy().hasHeightForWidth())
        self.push_button_refresh_midi_port.setSizePolicy(sizePolicy5)
        self.push_button_refresh_midi_port.setMinimumSize(QSize(0, 0))
        self.push_button_refresh_midi_port.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_16.addWidget(self.push_button_refresh_midi_port)


        self.horizontalLayout_14.addWidget(self.groupBox_5)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 1)
        self.horizontalLayout_14.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        main_window_sound_pad.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(main_window_sound_pad)
        self.statusBar.setObjectName(u"statusBar")
        main_window_sound_pad.setStatusBar(self.statusBar)

        self.retranslateUi(main_window_sound_pad)

        QMetaObject.connectSlotsByName(main_window_sound_pad)
    # setupUi

    def retranslateUi(self, main_window_sound_pad):
        main_window_sound_pad.setWindowTitle(QCoreApplication.translate("main_window_sound_pad", u"Sound Pad", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window_sound_pad", u"X-Axis", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Y-Axis", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Speed", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Pressure", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Press Event", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Release Event", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("main_window_sound_pad", u"MIDI Send", None))
        self.push_button_send_midi.setText(QCoreApplication.translate("main_window_sound_pad", u"Send", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Output MIDI Port", None))
        self.label_17.setText(QCoreApplication.translate("main_window_sound_pad", u"Port", None))
        self.push_button_refresh_midi_port.setText(QCoreApplication.translate("main_window_sound_pad", u"Refresh", None))
    # retranslateUi

