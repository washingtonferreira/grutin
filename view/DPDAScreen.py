# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from automatos.DPDA import *


class Ui_DPDAScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 235)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 0, 0))
        self.tableWidget.setObjectName("tableWidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 171, 16))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.teste)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.transition = {}
        self.dictionary = {}
        self.t1 = {}
        self.t2 = {}

    def creatTable(self, states, symbols, symbolsStack):
        self.verticalHeaderLabels = self.verticalSymbols(states, symbols, symbolsStack)
        # horizontalHeaderLabels = ['estado', 'pilha']
        horizontalHeaderLabels = ['estado']
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 278, 151))

        self.tableWidget.setColumnCount(len(horizontalHeaderLabels))
        self.tableWidget.setRowCount(len(self.verticalHeaderLabels))

        self.tableWidget.setHorizontalHeaderLabels(horizontalHeaderLabels)
        self.tableWidget.setVerticalHeaderLabels(self.verticalHeaderLabels)

        self.tableWidget.show()

    def c_current(self):
        states = sorted(self.states)
        symbols = sorted(self.symbols)

        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.tableWidget.item(row, col)
        value = value.text()

        string = str(self.verticalHeaderLabels[row])
        string = string.replace('(', '').replace(')', '').split(',')

        state = string[0].replace(' ', '')
        alphabet = string[1].replace(' ', '')
        stackSymble = string[2].replace(' ', '')

        value = self.getTuple(value)

        if value != '':
            if self.transition == {}:
                self.t1[stackSymble] = value
                self.t2[alphabet] = self.t1
                self.transition[state] = self.t2
            else:
                if state not in dict(self.transition).keys():
                    self.transition[state] = {alphabet: {stackSymble: value}}
                    print()
                if alphabet not in dict(self.transition[state]).keys():
                    self.transition[state][alphabet] = {stackSymble: value}
                    print()
                self.transition[state][alphabet][stackSymble] = value

        self.newField()

    def getTuple(self, value):
        x = value
        x += ','

        x = x.replace(' ', '').split(',')
        y = tuple(x[1])
        if y == ():
            y = ''
        if x[0] != '':
            value = (x[0], y)

        return value

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

        # self.transition = {'q0': {'a': {'0': ('q1', ('1', '0'))}},
        #                    'q2': {'': {'0': ('q3', ('0',))}, 'b': {'1': ('q2', '')}},
        #                    'q1': {'b': {'1': ('q2', '')}, 'a': {'1': ('q1', ('1', '1'))}}}


        pda = creatDPDA(self.states, self.symbols, self.symbolsStack, self.transition, self.initialState,
                        self.symbolsStackInitialself, self.finalStates)

        print([(state, stack.copy()) for state, stack in pda.validate_input('ab', step=True)])

        text = str([(state, stack.copy()) for state, stack in pda.validate_input('ab', step=True)])
        self.label.setText(text)

    def teste(self):
        self.states, self.symbols, self.symbolsStack, self.initialState, self.symbolsStackInitialself, \
        self.finalStates = definicaoFormal(self.lineEdit.text())

        self.creatTable(sorted(self.states), sorted(self.symbols), sorted(self.symbolsStack))
        self.tableWidget.cellChanged.connect(self.c_current)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn.setText(_translate("MainWindow", "click"))


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_DPDAScreen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
