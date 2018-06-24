# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import networkx as nx
import matplotlib.pyplot as plt
import random

from automatos.DFA import *


class Ui_AFDScreen(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 420)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(10, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.creatAFD)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(240, 40, 211, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setVisible(False)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 40, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, -10, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

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

        self.label_2.setVisible(False)

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

        self.tableWidget.setGeometry(QtCore.QRect(240, 40, 211, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

        self.tableWidget.setColumnCount(len(symbols))
        self.tableWidget.setRowCount(len(states))

        self.tableWidget.setHorizontalHeaderLabels(symbols)
        self.tableWidget.setVerticalHeaderLabels(states)
        
        self.tableWidget.show()
        self.label_2.setVisible(True)

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
        if self.isAFD:
            try:
                # self.transition = {
                #     'q0': {'0': 'q1', '1': 'q2'},
                #     'q1': {'0': 'q3', '1': 'q4'},
                #     'q2': {'0': 'q1', '1': 'q3'},
                #     'q3': {'0': 'q0', '1': 'q5'},
                #     'q4': {'0': 'q3', '1': 'q0'},
                #     'q5': {'0': 'q2', '1': 'q4'}
                # }

                self.dfa = creatDFA(self.states, self.symbols, self.initialState, self.finalStates, self.transition)

                text = retornaNormaPadrao(self.dfa, self.strInput.text())
                self.label.setText(text)
                self.label.setStyleSheet('color: black')

                if self.label.text() != "":
                    self.creatMenu()

                self.criarDiagrama()
            except Exception:
                self.mensagemDeErro('String invalida')

        else:
            self.isAFD = True
            self.creatAFD()
            self.run()

    def creatAFD(self):
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
                self.mensagemDeErro("Erro na insersão da definição formal")

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
        self.tableWidget.setGeometry(QtCore.QRect(240, 40, 211, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Tabela para inserir</p><p>a transição "
                                        "do</p><p>autômato finitio</p><p>deterministico</p></body></html>"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Automato Finito Deterministico"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))
        self.label_3.setText(_translate("MainWindow", "insira uma entrada na seguinte forma: \n"
                                                      "({q0, q1, q2}, {0,1}, d, {q0}, {q1})"))
        self.btn.setText(_translate("MainWindow", "click"))

    def mensagemDeErro(self, errorMessage):
        self.label.setStyleSheet('color: red')
        self.label.setText(errorMessage)

    def criarDiagrama(self):
        g = nx.Graph()

        for e in self.transition:
            for a in self.symbols:
                g.add_node(e, pos=(random.randint(0, 12), random.randint(0, 12)))
                g.add_edge(e, self.transition[e][a], weight=a)

        pos = nx.get_node_attributes(g, 'pos')
        nx.draw(g, pos, with_labels=True)
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AFDScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
