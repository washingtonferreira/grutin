# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

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
        self.btn.clicked.connect(self.creatAFND)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 20, 211, 151))
        self.tableWidget.setObjectName("tableWidget")

        self.strInput = QtWidgets.QLineEdit(self.centralwidget)
        self.strInput.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.strInput.setObjectName("strInput")

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnOK.clicked.connect(self.run)

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

        self.actionConverter_para_AFD = QtWidgets.QAction(MainWindow)
        self.actionConverter_para_AFD.setObjectName("actionConverter_para_AFD")
        self.actionConverter_para_AFD.triggered.connect(self.converterAFD)

        self.menuAFD.addAction(self.actionConverter_para_AFD)
        self.menuBar.addAction(self.menuAFD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.isAFND = True
        self.transition = {}
        self.temTransicao = False

    def converterAFD(self):
        if self.tableWidget.isVisible():
            self.resetTable()

        dfa = convertToDFA(self.nda)

        text = str(list(dfa.validate_input(self.strInput.text(), step=True)))

        self.label.setText('{}'.format(text))

        states = sorted(dfa.states)
        symbols = sorted(dfa.input_symbols)

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)

        for s in states:
            for sy in symbols:
                linha = states.index(str(s))
                coluna = symbols.index(str(sy))
                value = str(dfa.transitions[s][sy])
                self.tableWidget.setItem(linha, coluna, QTableWidgetItem(value))

        self.isAFND = False
        self.temTransicao = True

    def resetTable(self):
        self.tableWidget.clear()
        self.tableWidget.setDisabled(True)
        self.tableWidget.setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 211, 151))
        self.tableWidget.setObjectName("tableWidget")

        # self.tableWidget.setHorizontalHeaderLabels(symbols)
        # self.tableWidget.setVerticalHeaderLabels(states)

        self.tableWidget.show()
        # self.tableWidget.setDisabled(True)

    def creatTable(self, states, symbols):

        if self.tableWidget.isVisible():
            self.resetTable()

        symbols.append('')
        symbols = sorted(symbols)
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

        symbols.append('')
        symbols = sorted(symbols)

        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.tableWidget.item(row, col)
        value = str(value.text())

        if value != "":
            value = set(value.replace(' ', '').split(','))

            if self.transition == {}:
                self.transition[states[row]] = {symbols[col]: value}
            else:
                if states[row] not in self.transition.keys():
                    self.transition[states[row]] = {symbols[col]: value}
                else:
                    self.transition[states[row]][symbols[col]] = value

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
      if self.strInput.text() != "":
            if self.isAFND:
                self.nda = creatNFA(self.states, self.symbols, self.transition, self.initialState, self.finalStates)

                text = str(list(self.nda.validate_input(self.strInput.text(), step=True)))

                self.label.setText('{}'.format(text))

                if self.strInput != "":
                    self.creatMenu()
            else:
                self.isAFND = True
                self.creatAFND()
                self.run()

    def creatAFND(self):
        if self.lineEdit.text() != "":
            self.dictionary = {}

            self.states, self.symbols, self.initialState, self.finalStates = definicaoFormal(self.lineEdit.text())
            self.creatTable(sorted(self.states), sorted(self.symbols))

            if self.temTransicao:
                self.setTableValue(sorted(self.states), sorted(self.symbols))

            self.tableWidget.cellChanged.connect(self.c_current)

    def setTableValue(self, states, symbols):
        symbols.append('')
        symbols = sorted(symbols)

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)

        print('teste123')
        print(self.transition)
        print(self.nda.transitions)

        for s in states:
            for sy in symbols:
                linha = states.index(s)
                coluna = symbols.index(sy)
                if s in dict(self.nda.transitions).keys():
                    if sy in dict(self.nda.transitions[s]).keys():
                        value = QTableWidgetItem(str(self.nda.transitions[s][sy]))
                        self.tableWidget.setItem(linha, coluna, value)

    def creatMenu(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuAFD.setTitle(_translate("MainWindow", "AFND"))
        self.actionConverter_para_AFD.setText(_translate("MainWindow", "Converter para AFD"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn.setText(_translate("MainWindow", "click"))
        self.btnOK.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AFNDScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
