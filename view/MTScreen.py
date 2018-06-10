from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHeaderView

from automatos.MT import *


class Ui_MTScreen(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 270)
        MainWindow.setAnimated(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 5, 181, 31))
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 0, 0))
        self.tableWidget.setObjectName("tableWidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 491, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 30, 91, 138))
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEdit.setObjectName("definicao_formal")
        self.lineEdit.setPlaceholderText("({q0, q1, q2, q3, q4}, {0, 1}, {0, 1, x, y, .}, d , {q0}, {.}, {q4})")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setEnabled(True)
        self.btn.setGeometry(QtCore.QRect(20, 60, 75, 23))
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
                self.label.setText('Erro na inserção da definição formal')

    def resetTable(self):
        self.tableWidget.clear()
        self.tableWidget.setDisabled(True)
        self.tableWidget.setVisible(False)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 278, 151))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.show()

    def monta_tabela(self, estados, simbolos_fita):
        self.label_2.setVisible(True)

        if self.tableWidget.isVisible():
            self.resetTable()

        self.vertical_header_labels = self.coluna_estados(estados, simbolos_fita)
        horizontal_header_labels = ['(Estado, Simbolo, Fita)']
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 194, 151))

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
        self.strInput.setGeometry(QtCore.QRect(20, 110, 113, 20))
        self.strInput.setObjectName("strInput")
        self.strInput.setPlaceholderText('String de entrada!')
        self.strInput.show()

        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnOK.setText(_translate("MainWindow", "Ok"))
        self.btnOK.show()

        self.btnOK.clicked.connect(self.executa_maquina_turing)

    def executa_maquina_turing(self):
        if self.strInput.text() != "":
            try:

                m_turing = cria_maq_turing(self.estados, self.alfabeto, self.simbolos_fita, self.funcao_transicao,
                                           self.estado_inicial, self.simbolo_branco, self.estados_finais)

                transicao_criada = retorna_derivacao(m_turing, self.strInput.text())
                print(transicao_criada)
                self.label.setText(transicao_criada)
            except Exception:
                self.label.setText('String invalida')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maquina de Turing"))
        self.label.setText(_translate("MainWindow", ""))
        self.btn.setText(_translate("MainWindow", "click"))
        self.label_2.setText(_translate("MainWindow",
                                        '<html><head/><body><p>Taleba para inserir</p>'
                                        '<p>a transição do</p>'
                                        '<p>maquina de turing</p>'
                                        '</body></html>'))
        self.label_3.setText(_translate("MainWindow", "({q0, q1, q2, q3, q4}, {0, 1}, {0, 1, x, y, .}, d , {q0}, {.}, "
                                                      "{q4})"))

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MTScreen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
