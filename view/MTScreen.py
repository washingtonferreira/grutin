from PyQt5 import QtCore, QtWidgets
from automatos.MT import *


class Ui_MTScreen(object):
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
        self.lineEdit.setObjectName("definicao_formal")

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
        self.estados, self.alfabeto, self.simbolos_fita, self.estado_inicial, self.simbolo_branco, self.estados_finais \
            = definicao_formal(self.lineEdit.text())

        self.monta_tabela(sorted(self.estados), sorted(self.simbolos_fita))
        self.tableWidget.cellChanged.connect(self.c_current)

    def monta_tabela(self, estados, simbolos_fita):
        self.vertical_header_labels = self.coluna_estados(estados, simbolos_fita)
        horizontal_header_labels = ['Estados']
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 278, 151))

        self.tableWidget.setColumnCount(len(horizontal_header_labels))
        self.tableWidget.setRowCount(len(self.vertical_header_labels))

        self.tableWidget.setHorizontalHeaderLabels(horizontal_header_labels)
        self.tableWidget.setVerticalHeaderLabels(self.vertical_header_labels)

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

        print(value)

        value = tuple(value)

        print(value)
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
                    print()
                if simb_fita_atual not in dict(self.funcao_transicao[estado_atual]).keys():
                    self.funcao_transicao[estado_atual][simb_fita_atual] = value
                    print()

                self.funcao_transicao[estado_atual][simb_fita_atual] = value

            print(self.funcao_transicao)

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

        self.btnOK.clicked.connect(self.executa_maquina_turing)

    def executa_maquina_turing(self):
        m_turing = cria_maq_turing(self.estados, self.alfabeto, self.simbolos_fita, self.funcao_transicao,
                                   self.estado_inicial, self.simbolo_branco, self.estados_finais)

        transicao_criada = retorna_derivacao(m_turing, self.strInput.text())
        print(transicao_criada)
        self.label.setText(transicao_criada)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn.setText(_translate("MainWindow", "click"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MTScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())