# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem

from automatos.NFA import *


class Ui_AFNDScreen(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 400)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(20, 5, 181, 31))
        self.label_3.setGeometry(QtCore.QRect(10, -10, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 210, 531, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("({q0, q1, q2}, {a,b}, d, {q0}, {q1})")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(10, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.creatAFND)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 20, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setVisible(False)

        self.strInput = QtWidgets.QLineEdit(self.centralwidget)
        self.strInput.setGeometry(QtCore.QRect(10, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strInput.setFont(font)
        self.strInput.setText("")
        self.strInput.setObjectName("strInput")
        self.strInput.show()

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(140, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.btnOK.show()
        self.btnOK.clicked.connect(self.run)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 30, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)

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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.show()

    def creatTable(self, states, symbols):
        self.label_2.setVisible(True)

        if self.tableWidget.isVisible():
            self.resetTable()

        symbols.append('')
        symbols = sorted(symbols)
        symbols[0] = 'ε'

        self.tableWidget.setGeometry(QtCore.QRect(270, 20, 324, 115))

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
        self.strInput.setGeometry(QtCore.QRect(10, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strInput.setFont(font)
        self.strInput.setText("")
        self.strInput.setObjectName("strInput")
        self.strInput.show()

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(140, 130, 81, 31))
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
                if self.isAFND:
                    self.nda = creatNFA(self.states, self.symbols, self.transition, self.initialState, self.finalStates)

                    text = str(list(self.nda.validate_input(self.strInput.text(), step=True)))
                    self.label.setStyleSheet('color: black')

                    self.label.setText('{}'.format(text))

                    if self.strInput != "":
                        self.creatMenu()

            except Exception:
                self.mensagemDeErro('String invalida')

        else:
            self.isAFND = True
            self.creatAFND()
            self.run()

    def creatAFND(self):
        if self.lineEdit.text() != "":
            self.dictionary = {}

            try:
                self.states, self.symbols, self.initialState, self.finalStates = definicaoFormal(self.lineEdit.text())
                self.creatTable(sorted(self.states), sorted(self.symbols))

                if self.temTransicao:
                    self.setTableValue(sorted(self.states), sorted(self.symbols))

                self.tableWidget.cellChanged.connect(self.c_current)
                self.label.setText('')

            except Exception:
                self.mensagemDeErro('Erro na inserção da definição formal')

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Autômato Finito Não Deterministico"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))
        self.btnOK.setText(_translate("MainWindow", "Ok"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Tabela para inserir</p><p>a transição do</p><p>autômato"
                                        " finitio</p><p>não deterministico</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "insira uma entrada na seguinte forma: \n"
                                                      "({q0, q1, q2}, {a,b}, d, {q0}, {q1})"))

    def mensagemDeErro(self, errorMessage):
        self.label.setStyleSheet('color: red')
        self.label.setText(errorMessage)


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_AFNDScreen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
