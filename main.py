from UIbasic import Ui_Dialog
from matplotlib import pyplot as plt
import numpy as np
import sys
import math
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.added = 0
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign()
        self.show()
    def poly(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = float(self.ui.lineEdit_3.text())
        fig = plt.figure(figsize=(10, 10))  # Changes Graph Size
        ax = plt.axes(projection='3d')  # Calling for 3d projection using plt from Matlab library
        x = np.linspace(-20, 20, 1000)
        y = np.linspace(-20, 20, 1000)
        X, Y = np.meshgrid(x, y)
        z = Y**b + X**a + c
        ax.plot_surface(X, Y, z)
        plt.show()
    def exp(self):
        a = float(self.ui.lineEdit_4.text())
        e = math.e
        fig = plt.figure(figsize=(10, 10))  # Changes Graph Size
        ax = plt.axes(projection='3d')  # Calling for 3d projection using plt from Matlab library
        x = np.linspace(-20, 20, 1000)
        y = np.linspace(-20, 20, 1000)
        X, Y = np.meshgrid(x, y)
        z = e**(X * Y * a)
        ax.plot_surface(X, Y, z)
        plt.show()
    def rad(self):
        a = float(self.ui.lineEdit_5.text())
        b = float(self.ui.lineEdit_6.text())
        c = float(self.ui.lineEdit_7.text())
        fig = plt.figure(figsize=(10, 10))  # Changes Graph Size
        ax = plt.axes(projection='3d')  # Calling for 3d projection using plt from Matlab library
        x = np.linspace(-20, 20, 1000)
        y = np.linspace(-20, 20, 1000)
        X, Y = np.meshgrid(x, y)
        z = (Y * b + X * a + c)**0.5
        ax.plot_surface(X, Y, z)
        plt.show()
    def assign(self):
        self.ui.Poly.clicked.connect(self.poly)
        self.ui.Exp.clicked.connect(self.exp)
        self.ui.Rad.clicked.connect(self.rad)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())

main()

