# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_shot_control_widget.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_one_shot_control_widget(object):
    def setupUi(self, one_shot_control_widget):
        if not one_shot_control_widget.objectName():
            one_shot_control_widget.setObjectName(u"one_shot_control_widget")
        one_shot_control_widget.resize(400, 90)
        self.verticalLayout = QVBoxLayout(one_shot_control_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(one_shot_control_widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.combo_box_midi_type = QComboBox(one_shot_control_widget)
        self.combo_box_midi_type.setObjectName(u"combo_box_midi_type")

        self.horizontalLayout.addWidget(self.combo_box_midi_type)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(one_shot_control_widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_3)

        self.combo_box_channel = QComboBox(one_shot_control_widget)
        self.combo_box_channel.setObjectName(u"combo_box_channel")

        self.horizontalLayout.addWidget(self.combo_box_channel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_value_1 = QLabel(one_shot_control_widget)
        self.label_value_1.setObjectName(u"label_value_1")
        sizePolicy.setHeightForWidth(self.label_value_1.sizePolicy().hasHeightForWidth())
        self.label_value_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_value_1)

        self.combo_box_value_1 = QComboBox(one_shot_control_widget)
        self.combo_box_value_1.setObjectName(u"combo_box_value_1")

        self.horizontalLayout_2.addWidget(self.combo_box_value_1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_value_2 = QLabel(one_shot_control_widget)
        self.label_value_2.setObjectName(u"label_value_2")
        sizePolicy.setHeightForWidth(self.label_value_2.sizePolicy().hasHeightForWidth())
        self.label_value_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_value_2)

        self.combo_box_value_2 = QComboBox(one_shot_control_widget)
        self.combo_box_value_2.setObjectName(u"combo_box_value_2")

        self.horizontalLayout_2.addWidget(self.combo_box_value_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(one_shot_control_widget)

        QMetaObject.connectSlotsByName(one_shot_control_widget)
    # setupUi

    def retranslateUi(self, one_shot_control_widget):
        one_shot_control_widget.setWindowTitle(QCoreApplication.translate("one_shot_control_widget", u"OneShotControlWidget", None))
        self.label.setText(QCoreApplication.translate("one_shot_control_widget", u"MIDI Type", None))
        self.label_3.setText(QCoreApplication.translate("one_shot_control_widget", u"Channel", None))
        self.label_value_1.setText(QCoreApplication.translate("one_shot_control_widget", u"Value1", None))
        self.label_value_2.setText(QCoreApplication.translate("one_shot_control_widget", u"Value2", None))
    # retranslateUi

