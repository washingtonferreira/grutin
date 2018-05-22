# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from automatos.DFA import *


class Ui_AFDScreen(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 276)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 0, 0))
        self.tableWidget.setObjectName("tableWidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 491, 16))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.creatAFD)

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
        self.actionConverter_para_AFND.triggered.connect(self.converterAFND)

        self.menuAFD.addAction(self.actionConverter_para_AFND)
        self.menuBar.addAction(self.menuAFD.menuAction())

        self.retranslateUi(MainWindow)

        self.isAFD = True
        self.transition = {}
        self.temTransicao = False

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def creatMenu(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuAFD.setTitle(_translate("MainWindow", "Converter para AFND"))
        self.actionConverter_para_AFND.setText(_translate("MainWindow", "Converter para AFND"))

    def converterAFND(self):
        if self.tableWidget.isVisible():
            self.resetTable()

        self.nfa = convertToNFA(self.dfa)
        text = str(list(self.nfa.validate_input(self.strInput.text(), step=True)))

        self.label.setText(text)

        states = sorted(list(self.nfa.states))
        symbols = sorted(list(self.nfa.input_symbols))

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)

        for s in states:
            for sy in symbols:
                linha = states.index(s)
                coluna = symbols.index(sy)
                value = QTableWidgetItem(str(self.nfa.transitions[s][sy]))
                self.tableWidget.setItem(linha, coluna, value)

        self.isAFD = False
        self.temTransicao = True

    def creatTable(self, states, symbols):

        if self.tableWidget.isVisible():
            self.resetTable()

        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 211, 151))
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
        value = value.text()

        self.dictionary[symbols[col]] = value
        self.transition[states[row]] = self.dictionary

        if len(self.transition[states[row]]) == 2:
            self.dictionary = {}

        if len(self.transition) == len(states) and self.dictionary == {}:
            self.newField()


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
        if self.isAFD:
            self.dfa = creatDFA(self.states, self.symbols, self.initialState, self.finalStates, self.transition)

            text = str(list(self.dfa.validate_input(self.strInput.text(), step=True)))

            self.label.setText(text)

            if self.label.text() != "":
                self.creatMenu()
        else:
            self.isAFD = True
            self.creatAFD()
            self.run()

    def creatAFD(self):
        if self.lineEdit.text() != "":
            self.dictionary = {}

            self.states, self.symbols, self.initialState, self.finalStates = definicaoFormal(self.lineEdit.text())

            self.creatTable(sorted(self.states), sorted(self.symbols))

            if self.temTransicao:
                self.setTableValue(sorted(self.states), sorted(self.symbols))

            self.tableWidget.cellChanged.connect(self.c_current)

    def setTableValue(self, states, symbols):

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)

        for s in states:
            for sy in symbols:
                linha = states.index(s)
                coluna = symbols.index(sy)
                value = QTableWidgetItem(self.dfa.transitions[s][sy])
                self.tableWidget.setItem(linha, coluna, value)

    def resetTable(self):
        self.tableWidget.clear()
        self.tableWidget.setDisabled(True)
        self.tableWidget.setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 211, 151))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AFDScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
