# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIbasic.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 756)
        self.Poly = QtWidgets.QPushButton(Dialog)
        self.Poly.setGeometry(QtCore.QRect(50, 20, 101, 28))
        self.Poly.setObjectName("Poly")
        self.Exp = QtWidgets.QPushButton(Dialog)
        self.Exp.setGeometry(QtCore.QRect(340, 20, 111, 28))
        self.Exp.setObjectName("Exp")
        self.Rad = QtWidgets.QPushButton(Dialog)
        self.Rad.setGeometry(QtCore.QRect(622, 20, 101, 28))
        self.Rad.setObjectName("Rad")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(354, 80, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(580, 80, 181, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 150, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 31, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 31, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 210, 31, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 180, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 150, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(310, 150, 31, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(610, 150, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(580, 180, 31, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(610, 180, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 210, 113, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(580, 210, 31, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(580, 150, 31, 20))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Poly.setText(_translate("Dialog", "Plot Polynomial"))
        self.Exp.setText(_translate("Dialog", "Plot Exponential"))
        self.Rad.setText(_translate("Dialog", "Plot Radical"))
        self.label.setText(_translate("Dialog", "x^(a) + y^(b) + c"))
        self.label_2.setText(_translate("Dialog", "e^((a)*x*y)"))
        self.label_3.setText(_translate("Dialog", "((a)*x + (b)*y + (c))^(1/2)"))
        self.label_4.setText(_translate("Dialog", "a:"))
        self.label_5.setText(_translate("Dialog", "b:"))
        self.label_6.setText(_translate("Dialog", "c:"))
        self.label_7.setText(_translate("Dialog", "a:"))
        self.label_10.setText(_translate("Dialog", "b:"))
        self.label_11.setText(_translate("Dialog", "c:"))
        self.label_12.setText(_translate("Dialog", "a:"))

