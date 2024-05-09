# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realtime_control_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_realtime_control_widget(object):
    def setupUi(self, realtime_control_widget):
        if not realtime_control_widget.objectName():
            realtime_control_widget.setObjectName(u"realtime_control_widget")
        realtime_control_widget.resize(400, 90)
        self.verticalLayout = QVBoxLayout(realtime_control_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(realtime_control_widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.combo_box_midi_type = QComboBox(realtime_control_widget)
        self.combo_box_midi_type.setObjectName(u"combo_box_midi_type")

        self.horizontalLayout.addWidget(self.combo_box_midi_type)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(realtime_control_widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_3)

        self.combo_box_channel = QComboBox(realtime_control_widget)
        self.combo_box_channel.setObjectName(u"combo_box_channel")

        self.horizontalLayout.addWidget(self.combo_box_channel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(realtime_control_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.slider_sens = QSlider(realtime_control_widget)
        self.slider_sens.setObjectName(u"slider_sens")
        self.slider_sens.setMaximum(10000)
        self.slider_sens.setPageStep(1000)
        self.slider_sens.setValue(5000)
        self.slider_sens.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_sens)

        self.label_sens = QLabel(realtime_control_widget)
        self.label_sens.setObjectName(u"label_sens")
        self.label_sens.setMinimumSize(QSize(40, 0))
        self.label_sens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_sens)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(realtime_control_widget)

        QMetaObject.connectSlotsByName(realtime_control_widget)
    # setupUi

    def retranslateUi(self, realtime_control_widget):
        realtime_control_widget.setWindowTitle(QCoreApplication.translate("realtime_control_widget", u"RealtimeControlWidget", None))
        self.label.setText(QCoreApplication.translate("realtime_control_widget", u"MIDI Type", None))
        self.label_3.setText(QCoreApplication.translate("realtime_control_widget", u"Channel", None))
        self.label_2.setText(QCoreApplication.translate("realtime_control_widget", u"Sensitivity", None))
        self.label_sens.setText(QCoreApplication.translate("realtime_control_widget", u"1.00", None))
    # retranslateUi

