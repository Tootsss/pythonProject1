# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIpolynomial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UIpoly(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 314)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 111, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 121, 16))
        self.label_4.setObjectName("label_4")
        self.Co_a = QtWidgets.QLineEdit(Dialog)
        self.Co_a.setGeometry(QtCore.QRect(140, 100, 81, 22))
        self.Co_a.setObjectName("Co_a")
        self.Co_b = QtWidgets.QLineEdit(Dialog)
        self.Co_b.setGeometry(QtCore.QRect(140, 140, 81, 22))
        self.Co_b.setObjectName("Co_b")
        self.Co_c = QtWidgets.QLineEdit(Dialog)
        self.Co_c.setGeometry(QtCore.QRect(140, 180, 81, 22))
        self.Co_c.setObjectName("Co_c")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 101, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "x^(a) + y^(b) + c"))
        self.label_2.setText(_translate("Dialog", "a:"))
        self.label_3.setText(_translate("Dialog", "c:"))
        self.label_4.setText(_translate("Dialog", "b: "))
        self.pushButton.setText(_translate("Dialog", "Generate"))

