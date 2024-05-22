# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculate.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_calculate(object):
    def setupUi(self, calculate):
        if not calculate.objectName():
            calculate.setObjectName(u"calculate")
        calculate.resize(591, 486)
        self.layoutWidget = QWidget(calculate)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 30, 241, 206))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ShowResult = QLineEdit(self.layoutWidget)
        self.ShowResult.setObjectName(u"ShowResult")

        self.verticalLayout.addWidget(self.ShowResult)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Three = QPushButton(self.layoutWidget)
        self.Three.setObjectName(u"Three")

        self.gridLayout.addWidget(self.Three, 1, 2, 1, 1)

        self.Two = QPushButton(self.layoutWidget)
        self.Two.setObjectName(u"Two")

        self.gridLayout.addWidget(self.Two, 1, 1, 1, 1)

        self.One = QPushButton(self.layoutWidget)
        self.One.setObjectName(u"One")

        self.gridLayout.addWidget(self.One, 1, 0, 1, 1)

        self.Plus = QPushButton(self.layoutWidget)
        self.Plus.setObjectName(u"Plus")

        self.gridLayout.addWidget(self.Plus, 0, 1, 1, 1)

        self.Clear = QPushButton(self.layoutWidget)
        self.Clear.setObjectName(u"Clear")

        self.gridLayout.addWidget(self.Clear, 0, 0, 1, 1)

        self.Minus = QPushButton(self.layoutWidget)
        self.Minus.setObjectName(u"Minus")

        self.gridLayout.addWidget(self.Minus, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.Result = QPushButton(self.layoutWidget)
        self.Result.setObjectName(u"Result")

        self.verticalLayout.addWidget(self.Result)


        self.retranslateUi(calculate)

        QMetaObject.connectSlotsByName(calculate)
    # setupUi

    def retranslateUi(self, calculate):
        calculate.setWindowTitle(QCoreApplication.translate("calculate", u"Form", None))
        self.Three.setText(QCoreApplication.translate("calculate", u"3", None))
        self.Two.setText(QCoreApplication.translate("calculate", u"2", None))
        self.One.setText(QCoreApplication.translate("calculate", u"1", None))
        self.Plus.setText(QCoreApplication.translate("calculate", u"+", None))
        self.Clear.setText(QCoreApplication.translate("calculate", u"C", None))
        self.Minus.setText(QCoreApplication.translate("calculate", u"-", None))
        self.Result.setText(QCoreApplication.translate("calculate", u"=", None))
    # retranslateUi

