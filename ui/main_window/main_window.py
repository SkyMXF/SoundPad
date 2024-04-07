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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_main_window_sound_pad(object):
    def setupUi(self, main_window_sound_pad):
        if not main_window_sound_pad.objectName():
            main_window_sound_pad.setObjectName(u"main_window_sound_pad")
        main_window_sound_pad.resize(1600, 900)
        self.centralwidget = QWidget(main_window_sound_pad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_control_panel = QFrame(self.centralwidget)
        self.frame_control_panel.setObjectName(u"frame_control_panel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_control_panel.sizePolicy().hasHeightForWidth())
        self.frame_control_panel.setSizePolicy(sizePolicy)
        self.frame_control_panel.setMouseTracking(True)
        self.frame_control_panel.setFocusPolicy(Qt.NoFocus)
        self.frame_control_panel.setFrameShape(QFrame.StyledPanel)
        self.frame_control_panel.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_control_panel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label)

        self.combo_box_midi_cc_x_axis = QComboBox(self.groupBox)
        self.combo_box_midi_cc_x_axis.setObjectName(u"combo_box_midi_cc_x_axis")

        self.horizontalLayout_6.addWidget(self.combo_box_midi_cc_x_axis)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.combo_box_chn_x_axis = QComboBox(self.groupBox)
        self.combo_box_chn_x_axis.setObjectName(u"combo_box_chn_x_axis")

        self.horizontalLayout_6.addWidget(self.combo_box_chn_x_axis)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.slider_sens_x_axis = QSlider(self.groupBox)
        self.slider_sens_x_axis.setObjectName(u"slider_sens_x_axis")
        self.slider_sens_x_axis.setMaximum(10000)
        self.slider_sens_x_axis.setPageStep(1000)
        self.slider_sens_x_axis.setValue(5000)
        self.slider_sens_x_axis.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_sens_x_axis)

        self.label_x_axis_sens = QLabel(self.groupBox)
        self.label_x_axis_sens.setObjectName(u"label_x_axis_sens")
        self.label_x_axis_sens.setMinimumSize(QSize(40, 0))
        self.label_x_axis_sens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_x_axis_sens)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_11.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.combo_box_midi_cc_y_axis = QComboBox(self.groupBox_2)
        self.combo_box_midi_cc_y_axis.setObjectName(u"combo_box_midi_cc_y_axis")

        self.horizontalLayout_7.addWidget(self.combo_box_midi_cc_y_axis)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.combo_box_chn_y_axis = QComboBox(self.groupBox_2)
        self.combo_box_chn_y_axis.setObjectName(u"combo_box_chn_y_axis")

        self.horizontalLayout_7.addWidget(self.combo_box_chn_y_axis)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.slider_sens_y_axis = QSlider(self.groupBox_2)
        self.slider_sens_y_axis.setObjectName(u"slider_sens_y_axis")
        self.slider_sens_y_axis.setMaximum(10000)
        self.slider_sens_y_axis.setPageStep(1000)
        self.slider_sens_y_axis.setValue(5000)
        self.slider_sens_y_axis.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_sens_y_axis)

        self.label_y_axis_sens = QLabel(self.groupBox_2)
        self.label_y_axis_sens.setObjectName(u"label_y_axis_sens")
        self.label_y_axis_sens.setMinimumSize(QSize(40, 0))
        self.label_y_axis_sens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_y_axis_sens)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_11.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.combo_box_midi_cc_speed = QComboBox(self.groupBox_3)
        self.combo_box_midi_cc_speed.setObjectName(u"combo_box_midi_cc_speed")

        self.horizontalLayout_8.addWidget(self.combo_box_midi_cc_speed)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.combo_box_chn_speed = QComboBox(self.groupBox_3)
        self.combo_box_chn_speed.setObjectName(u"combo_box_chn_speed")

        self.horizontalLayout_8.addWidget(self.combo_box_chn_speed)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.slider_sens_speed = QSlider(self.groupBox_3)
        self.slider_sens_speed.setObjectName(u"slider_sens_speed")
        self.slider_sens_speed.setMaximum(10000)
        self.slider_sens_speed.setPageStep(1000)
        self.slider_sens_speed.setValue(5000)
        self.slider_sens_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.slider_sens_speed)

        self.label_speed_sens = QLabel(self.groupBox_3)
        self.label_speed_sens.setObjectName(u"label_speed_sens")
        self.label_speed_sens.setMinimumSize(QSize(40, 0))
        self.label_speed_sens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_speed_sens)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_11.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.combo_box_midi_cc_pressure = QComboBox(self.groupBox_4)
        self.combo_box_midi_cc_pressure.setObjectName(u"combo_box_midi_cc_pressure")

        self.horizontalLayout_9.addWidget(self.combo_box_midi_cc_pressure)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.combo_box_chn_pressure = QComboBox(self.groupBox_4)
        self.combo_box_chn_pressure.setObjectName(u"combo_box_chn_pressure")

        self.horizontalLayout_9.addWidget(self.combo_box_chn_pressure)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.slider_sens_pressure = QSlider(self.groupBox_4)
        self.slider_sens_pressure.setObjectName(u"slider_sens_pressure")
        self.slider_sens_pressure.setMaximum(10000)
        self.slider_sens_pressure.setPageStep(1000)
        self.slider_sens_pressure.setValue(5000)
        self.slider_sens_pressure.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.slider_sens_pressure)

        self.label_pressure_sens = QLabel(self.groupBox_4)
        self.label_pressure_sens.setObjectName(u"label_pressure_sens")
        self.label_pressure_sens.setMinimumSize(QSize(40, 0))
        self.label_pressure_sens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_pressure_sens)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_11.addWidget(self.groupBox_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.label_18)

        self.combo_box_midi_cc_press = QComboBox(self.groupBox_7)
        self.combo_box_midi_cc_press.setObjectName(u"combo_box_midi_cc_press")
        sizePolicy4.setHeightForWidth(self.combo_box_midi_cc_press.sizePolicy().hasHeightForWidth())
        self.combo_box_midi_cc_press.setSizePolicy(sizePolicy4)

        self.horizontalLayout_15.addWidget(self.combo_box_midi_cc_press)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.label_22)

        self.combo_box_value_press = QComboBox(self.groupBox_7)
        self.combo_box_value_press.setObjectName(u"combo_box_value_press")
        sizePolicy4.setHeightForWidth(self.combo_box_value_press.sizePolicy().hasHeightForWidth())
        self.combo_box_value_press.setSizePolicy(sizePolicy4)

        self.horizontalLayout_15.addWidget(self.combo_box_value_press)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.label_19)

        self.combo_box_chn_press = QComboBox(self.groupBox_7)
        self.combo_box_chn_press.setObjectName(u"combo_box_chn_press")
        sizePolicy4.setHeightForWidth(self.combo_box_chn_press.sizePolicy().hasHeightForWidth())
        self.combo_box_chn_press.setSizePolicy(sizePolicy4)

        self.horizontalLayout_15.addWidget(self.combo_box_chn_press)


        self.horizontalLayout_14.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.label_20)

        self.combo_box_midi_cc_release = QComboBox(self.groupBox_6)
        self.combo_box_midi_cc_release.setObjectName(u"combo_box_midi_cc_release")
        sizePolicy4.setHeightForWidth(self.combo_box_midi_cc_release.sizePolicy().hasHeightForWidth())
        self.combo_box_midi_cc_release.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.combo_box_midi_cc_release)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.label_23)

        self.combo_box_value_release = QComboBox(self.groupBox_6)
        self.combo_box_value_release.setObjectName(u"combo_box_value_release")
        sizePolicy4.setHeightForWidth(self.combo_box_value_release.sizePolicy().hasHeightForWidth())
        self.combo_box_value_release.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.combo_box_value_release)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.label_21)

        self.combo_box_chn_release = QComboBox(self.groupBox_6)
        self.combo_box_chn_release.setObjectName(u"combo_box_chn_release")
        sizePolicy4.setHeightForWidth(self.combo_box_chn_release.sizePolicy().hasHeightForWidth())
        self.combo_box_chn_release.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.combo_box_chn_release)


        self.horizontalLayout_14.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setMinimumSize(QSize(350, 0))
        self.groupBox_5.setMaximumSize(QSize(350, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.combo_box_midi_port = QComboBox(self.groupBox_5)
        self.combo_box_midi_port.setObjectName(u"combo_box_midi_port")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combo_box_midi_port.sizePolicy().hasHeightForWidth())
        self.combo_box_midi_port.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.combo_box_midi_port)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)

        self.push_button_refresh_midi_port = QPushButton(self.groupBox_5)
        self.push_button_refresh_midi_port.setObjectName(u"push_button_refresh_midi_port")
        sizePolicy2.setHeightForWidth(self.push_button_refresh_midi_port.sizePolicy().hasHeightForWidth())
        self.push_button_refresh_midi_port.setSizePolicy(sizePolicy2)
        self.push_button_refresh_midi_port.setMinimumSize(QSize(0, 0))
        self.push_button_refresh_midi_port.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_16.addWidget(self.push_button_refresh_midi_port)


        self.horizontalLayout_14.addWidget(self.groupBox_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.label.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_13.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.label_2.setText(QCoreApplication.translate("main_window_sound_pad", u"Sensitivity", None))
        self.label_x_axis_sens.setText(QCoreApplication.translate("main_window_sound_pad", u"1.00", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Y-Axis", None))
        self.label_3.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_14.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.label_4.setText(QCoreApplication.translate("main_window_sound_pad", u"Sensitivity", None))
        self.label_y_axis_sens.setText(QCoreApplication.translate("main_window_sound_pad", u"1.00", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Speed", None))
        self.label_5.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_15.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.label_6.setText(QCoreApplication.translate("main_window_sound_pad", u"Sensitivity", None))
        self.label_speed_sens.setText(QCoreApplication.translate("main_window_sound_pad", u"1.00", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Pressure", None))
        self.label_7.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_16.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.label_8.setText(QCoreApplication.translate("main_window_sound_pad", u"Sensitivity", None))
        self.label_pressure_sens.setText(QCoreApplication.translate("main_window_sound_pad", u"1.00", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Press Event", None))
        self.label_18.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_22.setText(QCoreApplication.translate("main_window_sound_pad", u"Value", None))
        self.label_19.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Release Event", None))
        self.label_20.setText(QCoreApplication.translate("main_window_sound_pad", u"MIDI CC", None))
        self.label_23.setText(QCoreApplication.translate("main_window_sound_pad", u"Value", None))
        self.label_21.setText(QCoreApplication.translate("main_window_sound_pad", u"Channel", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("main_window_sound_pad", u"Output MIDI Port", None))
        self.label_17.setText(QCoreApplication.translate("main_window_sound_pad", u"Port", None))
        self.push_button_refresh_midi_port.setText(QCoreApplication.translate("main_window_sound_pad", u"Refresh", None))
    # retranslateUi

