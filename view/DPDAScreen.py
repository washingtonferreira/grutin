# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QHeaderView

from automatos.DPDA import *


class Ui_DPDAScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 350)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 291, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 0, 0))
        self.tableWidget.setObjectName("tableWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 210, 531, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 40, 150, 180))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("({q0, q1, q2, q3}, {a, b}, {0, 1}, {q0}, {0}, {q3})")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(20, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.creatDPDA)

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

    def resetTable(self):
        self.tableWidget.clear()
        self.tableWidget.setDisabled(True)
        self.tableWidget.setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 0, 0))
        self.tableWidget.setObjectName("tableWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

    def creatTable(self, states, symbols, symbolsStack):
        self.label_2.setVisible(True)

        if self.tableWidget.isVisible():
            self.resetTable()

        self.verticalHeaderLabels = self.verticalSymbols(states, symbols, symbolsStack)
        # horizontalHeaderLabels = ['estado', 'pilha']
        horizontalHeaderLabels = ['(estado, leitura, pilha)']
        self.tableWidget.setGeometry(QtCore.QRect(280, 40, 255, 151))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.tableWidget.setFont(font)

        self.tableWidget.setColumnCount(len(horizontalHeaderLabels))
        self.tableWidget.setRowCount(len(self.verticalHeaderLabels))

        self.tableWidget.setHorizontalHeaderLabels(horizontalHeaderLabels)
        self.tableWidget.setVerticalHeaderLabels(self.verticalHeaderLabels)
        self.tableWidget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

        self.tableWidget.show()

    def verticalSymbols(self, states, input_symbols, stack_symbols):
        teste = []
        for s in states:
            for sa in input_symbols:
                for ss in stack_symbols:
                    c = '({}, {}, {})'.format(s, sa, ss)
                    teste.append(c)
        return teste

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

        if value != '':
            value = self.getTuple(value)
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
        self.strInput.setGeometry(QtCore.QRect(20, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strInput.setFont(font)
        self.strInput.setText("")
        self.strInput.setObjectName("strInput")
        self.strInput.show()

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(150, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.btnOK.setText(_translate("MainWindow", "Ok"))
        self.btnOK.show()

        self.btnOK.clicked.connect(self.run)

    def run(self):
        if self.strInput.text() != "":
            try:
                # self.transition = {
                #     'q0': {
                #         'a': {'0': ('q1', ('1', '0'))}  # transition pushes '1' to stack
                #     },
                #     'q1': {
                #         'a': {'1': ('q1', ('1', '1'))},
                #         'b': {'1': ('q2', '')}  # transition pops from stack
                #     },
                #     'q2': {
                #         'b': {'1': ('q2', '')},
                #         '': {'0': ('q3', ('0',))}  # transition does not change stack
                #     }
                # }

                pda = creatDPDA(self.states, self.symbols, self.symbolsStack, self.transition, self.initialState,
                                self.symbolsStackInitialself, self.finalStates)

                # print([(state, stack.copy()) for state, stack in pda.validate_input(self.strInput.text(), step=True)])

                text = str(
                    [(state, stack.copy()) for state, stack in pda.validate_input(self.strInput.text(), step=True)])
                self.label.setStyleSheet('color: black')

                self.label.setText(text)
            except Exception:
                self.mensagemDeErro('String invalida')

    def creatDPDA(self):
        if self.lineEdit.text() != "":

            try:
                self.states, self.symbols, self.symbolsStack, self.initialState, self.symbolsStackInitialself, \
                self.finalStates = definicaoFormal(self.lineEdit.text())

                self.creatTable(sorted(self.states), sorted(self.symbols), sorted(self.symbolsStack))
                self.tableWidget.cellChanged.connect(self.c_current)

                self.label.setText('')

            except Exception:
                self.mensagemDeErro('Erro na inserção da definição formal')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autômato Com Pilha"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Tabela para inserir</p>"
                                        "<p>a transição do</p>"
                                        "<p>autômato de pilha</p>"
                                        "<p>(q1, 1, 0)</p>"
                                        "<p>(q1, 1,)</p>"
                                        "<p>(q1, )</p>""</body></html>"))
        self.label_3.setText(_translate("MainWindow", "insira uma entrada na seguinte forma: \n"
                                                      "({q0, q1, q2, q3}, {a, b}, {0, 1}, \n{q0}, {0}, {q3})"))

    def mensagemDeErro(self, errorMessage):
        self.label.setStyleSheet('color: red')
        self.label.setText(errorMessage)

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_DPDAScreen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
