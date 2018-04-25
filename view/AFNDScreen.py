# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from automatos.NFA import *

class Ui_AFNDScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 234)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 160, 241, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.btn.setObjectName("btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 20, 211, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.strInput = QtWidgets.QLineEdit(self.centralwidget)
        self.strInput.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.strInput.setObjectName("strInput")
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.btnOK.setObjectName("btnOK")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 535, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuAFD = QtWidgets.QMenu(self.menuBar)
        self.menuAFD.setObjectName("menuAFD")
        MainWindow.setMenuBar(self.menuBar)
        self.actionConverter_para_AFND = QtWidgets.QAction(MainWindow)
        self.actionConverter_para_AFND.setObjectName("actionConverter_para_AFND")
        self.menuAFD.addAction(self.actionConverter_para_AFND)
        self.menuBar.addAction(self.menuAFD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def creatTable(self, states, symbols):
        symbols[0] = 'vazio'
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 324, 115))

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)

        self.tableWidget.show()

    def c_current(self):
        states = sorted(self.states)
        symbols = sorted(self.symbols)

        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.tableWidget.item(row, col)
        value = str(value.text())
        value = set(value.replace(' ', '').split(','))

        self.dictionary[symbols[col]] = value
        self.transition[states[row]] = self.dictionary

        if len(self.transition[states[row]]) == 3:
            self.dictionary = {}

        if len(self.transition) == len(states) and self.dictionary == {}:
            print(self.transition)
            print()

            for estado in self.transition:
                for x in self.transition[estado]:
                    if self.transition[estado][x] == {''}:
                        print(self.transition[estado])
                    else:
                        print(self.transition[estado][x])

            print(self.transition)
        # self.newField()

    # ({q1, q2, q3}, {0,1,}, {q1}, {q3})
    def newField(self):
        _translate = QtCore.QCoreApplication.translate

        self.strInput = QtWidgets.QLineEdit(self.centralwidget)
        self.strInput.setGeometry(QtCore.QRect(20, 110, 113, 20))
        self.strInput.setObjectName("strInput")
        self.strInput.show()

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnOK.setText(_translate("MainWindow", "Ok"))
        self.btnOK.show()

        self.btnOK.clicked.connect(self.run)

    def run(self):

        dfa = creatNFA(self.states, self.symbols, self.transition,  self.initialState, self.finalStates)

        text = str(list(dfa.validate_input(self.strInput.text(), step=True)))

        self.label.setText(text)

    def teste(self):
        self.transition = {}
        self.dictionary = {}

        self.states, self.symbols, self.initialState, self.finalStates = definicaoFormal(self.lineEdit.text())
        self.creatTable(sorted(self.states), sorted(self.symbols))
        self.tableWidget.cellChanged.connect(self.c_current)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn.setText(_translate("MainWindow", "click"))
        self.btnOK.setText(_translate("MainWindow", "Ok"))
        self.menuAFD.setTitle(_translate("MainWindow", "AFND"))
        self.actionConverter_para_AFND.setText(_translate("MainWindow", "Converter para AFD"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AFNDScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
