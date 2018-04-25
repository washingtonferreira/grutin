# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from view.AFDScreen import Ui_AFDScreen
from view.AFNDScreen import Ui_AFNDScreen
from view.DPDAScreen import Ui_DPDAScreen

class Ui_MainWindow(object):
    def openAFDScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AFDScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAFNDScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AFNDScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDPDAScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DPDAScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName("menubar")

        self.menu_automatos = QtWidgets.QMenu(self.menubar)
        self.menu_automatos.setObjectName("menu_automatos")
        # self.menu_automatos.triggered.connect(self.callAFDScreen)  # add função ao menu

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionAFD = QtWidgets.QAction(MainWindow)
        self.actionAFD.setObjectName("actionAFD")
        self.actionAFD.triggered.connect(self.callAFDScreen)

        self.actionAFND = QtWidgets.QAction(MainWindow)
        self.actionAFND.setObjectName("actionAFND")
        self.actionAFND.triggered.connect(self.callAFNDScreen)

        self.actionPDA = QtWidgets.QAction(MainWindow)
        self.actionPDA.setObjectName("actionPDA")
        self.actionPDA.triggered.connect(self.callPDAScreen)


        self.menu_automatos.addAction(self.actionAFD)
        self.menu_automatos.addAction(self.actionAFND)
        self.menu_automatos.addAction(self.actionPDA)
        self.menubar.addAction(self.menu_automatos.menuAction())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def callAFDScreen(self):
        self.openAFDScreen()

    def callAFNDScreen(self):
        self.openAFNDScreen()

    def callPDAScreen(self):
        self.openDPDAScreen()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_automatos.setTitle(_translate("MainWindow", "Autômatos"))
        self.actionAFD.setText(_translate("MainWindow", "AFD"))
        self.actionAFND.setText(_translate("MainWindow", "AFND"))
        self.actionPDA.setText(_translate("MainWindow", "PDA"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
