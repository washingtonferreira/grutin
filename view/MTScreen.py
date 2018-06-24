from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QHeaderView

from automatos.MT import *


class Ui_MTScreen(object):
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
        self.lineEdit.setPlaceholderText("({q0, q1, q2, q3, q4}, {0, 1}, {0, 1, x, y, .}, d , {q0}, {.}, {q4})")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(20, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.criar_tabela_transicao)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.funcao_transicao = {}
        self.t1 = {}
        self.t2 = {}

    def criar_tabela_transicao(self):
        if self.lineEdit.text() != "":

            try:
                self.estados, self.alfabeto, self.simbolos_fita, self.estado_inicial, self.simbolo_branco, self.estados_finais \
                    = definicao_formal(self.lineEdit.text())

                self.monta_tabela(sorted(self.estados), sorted(self.simbolos_fita))
                self.tableWidget.cellChanged.connect(self.c_current)
                self.label.setText('')
            except Exception:
                self.mensagemDeErro('Erro na inserção da definição formal')

    def resetTable(self):
        self.tableWidget.clear()
        self.tableWidget.setDisabled(True)
        self.tableWidget.setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 278, 151))
        self.tableWidget.setObjectName("tableWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)


        self.tableWidget.show()

    def monta_tabela(self, estados, simbolos_fita):
        self.label_2.setVisible(True)

        if self.tableWidget.isVisible():
            self.resetTable()

        self.vertical_header_labels = self.coluna_estados(estados, simbolos_fita)
        horizontal_header_labels = ['(Estado, Simbolo, Fita)']
        self.tableWidget.setGeometry(QtCore.QRect(280, 40, 255, 151))

        self.tableWidget.setColumnCount(len(horizontal_header_labels))
        self.tableWidget.setRowCount(len(self.vertical_header_labels))

        self.tableWidget.setHorizontalHeaderLabels(horizontal_header_labels)
        self.tableWidget.setVerticalHeaderLabels(self.vertical_header_labels)
        self.tableWidget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

        self.tableWidget.show()

    def coluna_estados(self, estados, simbolos_fita):
        estado_simbolo = []

        for e in estados:
            for s in simbolos_fita:
                est_sim = '({},{}): '.format(e, s)
                estado_simbolo.append(est_sim)
        return estado_simbolo

    def c_current(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.tableWidget.item(row, col).text()
        value = value.replace('(', '').replace(')', '').replace(' ', '').split(',')

        if value != '':
            value = tuple(value)
            if value != ('',):
                string = str(self.vertical_header_labels[row])
                string = string.replace('(', '').replace(')', '').replace(' ', '').replace(':', '').split(',')

                estado_atual = string[0]
                simb_fita_atual = string[1]

                if self.funcao_transicao == {}:
                    self.funcao_transicao[estado_atual] = {simb_fita_atual: value}
                else:
                    if estado_atual not in dict(self.funcao_transicao).keys():
                        self.funcao_transicao[estado_atual] = {simb_fita_atual: value}

                    if simb_fita_atual not in dict(self.funcao_transicao[estado_atual]).keys():
                        self.funcao_transicao[estado_atual][simb_fita_atual] = value

                    self.funcao_transicao[estado_atual][simb_fita_atual] = value

                    # print(self.funcao_transicao)

        self.newField()

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

        self.btnOK.clicked.connect(self.executa_maquina_turing)

    def executa_maquina_turing(self):
        if self.strInput.text() != "":
            try:

                self.funcao_transicao = {
                    'q0': {
                        '0': ('q1', 'x', 'R'),
                        'y': ('q3', 'y', 'R')
                    },
                    'q1': {
                        '0': ('q1', '0', 'R'),
                        '1': ('q2', 'y', 'L'),
                        'y': ('q1', 'y', 'R')
                    },
                    'q2': {
                        '0': ('q2', '0', 'L'),
                        'x': ('q0', 'x', 'R'),
                        'y': ('q2', 'y', 'L')
                    },
                    'q3': {
                        'y': ('q3', 'y', 'R'),
                        '.': ('q4', '.', 'R')
                    }
                }

                m_turing = cria_maq_turing(self.estados, self.alfabeto, self.simbolos_fita, self.funcao_transicao,
                                           self.estado_inicial, self.simbolo_branco, self.estados_finais)

                transicao_criada = retorna_derivacao(m_turing, self.strInput.text())
                self.label.setStyleSheet('color: black')

                self.label.setText(transicao_criada)
            except Exception:
                self.mensagemDeErro('String invalida')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maquina de Turing"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))
        self.label_2.setText(_translate("MainWindow",
                                        '<html><head/><body><p>Tabela para inserir</p>'
                                        '<p>a transição do</p>'
                                        '<p>maquina de turing</p>'
                                        '</body></html>'))
        self.label_3.setText(_translate("MainWindow", "insira uma entrada na seguinte forma: \n"
                                                      "({q0, q1, q2, q3, q4}, {0, 1}, \n"
                                                      "{0, 1, x, y, .}, d , {q0}, {.}, "
                                                      "{q4})"))

    def mensagemDeErro(self, errorMessage):
        self.label.setStyleSheet('color: red')
        self.label.setText(errorMessage)

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MTScreen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
