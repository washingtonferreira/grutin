import re

from automatos.cfg import CFG
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox


class Ui_GLCScreen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(678, 500)
        Form.setAnimated(False)

        self.txt_def_formal = QtWidgets.QLineEdit(Form)
        self.txt_def_formal.setGeometry(QtCore.QRect(20, 20, 251, 21))
        self.txt_def_formal.setObjectName("txt_def_formal")

        self.txt_simbolo_vazio = QtWidgets.QLineEdit(Form)
        self.txt_simbolo_vazio.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.txt_simbolo_vazio.setObjectName("txt_simbolo_vazio")

        self.lbl_simbolo_vazio = QtWidgets.QLabel(Form)
        self.lbl_simbolo_vazio.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.lbl_simbolo_vazio.setObjectName("lbl_simbolo_vazio")

        self.btn_validar_glc = QtWidgets.QPushButton(Form)
        self.btn_validar_glc.setGeometry(QtCore.QRect(20, 340, 251, 31))
        self.btn_validar_glc.setObjectName("btn_validar_glc")

        self.table_funcao_transicao = QtWidgets.QTableWidget(Form)
        self.table_funcao_transicao.setEnabled(False)
        self.table_funcao_transicao.setGeometry(QtCore.QRect(20, 90, 251, 241))
        self.table_funcao_transicao.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.table_funcao_transicao.setObjectName("table_funcao_transicao")
        self.table_funcao_transicao.setColumnCount(0)
        self.table_funcao_transicao.setRowCount(0)

        self.btn_valida_def_formal = QtWidgets.QPushButton(Form)
        self.btn_valida_def_formal.setEnabled(False)
        self.btn_valida_def_formal.setGeometry(QtCore.QRect(140, 50, 131, 31))
        self.btn_valida_def_formal.setObjectName("btn_valida_def_formal")

        self.btn_producoes_vazias = QtWidgets.QPushButton(Form)
        self.btn_producoes_vazias.setGeometry(QtCore.QRect(20, 380, 141, 31))
        self.btn_producoes_vazias.setObjectName("btn_producoes_vazias")

        self.btn_producoes_inuteis = QtWidgets.QPushButton(Form)
        self.btn_producoes_inuteis.setGeometry(QtCore.QRect(170, 380, 101, 31))
        self.btn_producoes_inuteis.setObjectName("btn_producoes_inuteis")

        self.btn_fnc = QtWidgets.QPushButton(Form)
        self.btn_fnc.setGeometry(QtCore.QRect(20, 420, 251, 31))
        self.btn_fnc.setObjectName("btn_fnc")

        self.txt_string_validacao = QtWidgets.QLineEdit(Form)
        self.txt_string_validacao.setGeometry(QtCore.QRect(20, 460, 121, 21))
        self.txt_string_validacao.setObjectName("txt_string_validacao")

        self.btn_validar_string = QtWidgets.QPushButton(Form)
        self.btn_validar_string.setGeometry(QtCore.QRect(150, 460, 121, 23))
        self.btn_validar_string.setObjectName("btn_validar_string")

        self.txt_procuoes_vazias = QtWidgets.QTextEdit(Form)
        self.txt_procuoes_vazias.setEnabled(False)
        self.txt_procuoes_vazias.setGeometry(QtCore.QRect(280, 40, 191, 201))
        self.txt_procuoes_vazias.setObjectName("txt_procuoes_vazias")

        self.txt_producoes_inuteis = QtWidgets.QTextEdit(Form)
        self.txt_producoes_inuteis.setEnabled(False)
        self.txt_producoes_inuteis.setGeometry(QtCore.QRect(480, 40, 191, 201))
        self.txt_producoes_inuteis.setObjectName("txt_producoes_inuteis")

        self.txt_fnc = QtWidgets.QTextEdit(Form)
        self.txt_fnc.setEnabled(False)
        self.txt_fnc.setGeometry(QtCore.QRect(370, 270, 191, 211))
        self.txt_fnc.setObjectName("txt_fnc")

        self.lb_producoes_vazias = QtWidgets.QLabel(Form)
        self.lb_producoes_vazias.setEnabled(False)
        self.lb_producoes_vazias.setGeometry(QtCore.QRect(290, 20, 181, 20))
        self.lb_producoes_vazias.setObjectName("lb_producoes_vazias")

        self.lbl_producoes_inuteis = QtWidgets.QLabel(Form)
        self.lbl_producoes_inuteis.setEnabled(False)
        self.lbl_producoes_inuteis.setGeometry(QtCore.QRect(490, 20, 181, 20))
        self.lbl_producoes_inuteis.setObjectName("lbl_producoes_inuteis")

        self.lbl_fnc = QtWidgets.QLabel(Form)
        self.lbl_fnc.setEnabled(False)
        self.lbl_fnc.setGeometry(QtCore.QRect(380, 250, 181, 20))
        self.lbl_fnc.setObjectName("lbl_fnc")

        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.btn_producoes_inuteis.setEnabled(False)
        self.btn_producoes_vazias.setEnabled(False)
        self.txt_string_validacao.setEnabled(False)
        self.btn_valida_def_formal.setEnabled(True)
        self.btn_validar_string.setEnabled(False)
        self.btn_validar_glc.setEnabled(False)
        self.btn_fnc.setEnabled(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def set_txt_producoes_vazias(self, producoes_vazias_texto):
        self.txt_procuoes_vazias.setText(producoes_vazias_texto)

    def set_txt_producoes_inuteis(self, producoes_inuteis_texto):
        self.txt_producoes_inuteis.setText(producoes_inuteis_texto)

    def set_txt_fnc(self, forma_normal_chomsky_txt):
        self.txt_fnc.setText(forma_normal_chomsky_txt)

    def monta_objetos_glc(self, definicao_formal, simbolo_vazio):
        ativo = self.btn_valida_def_formal.isEnabled()

        if ativo:
            def_formal_array = re.findall('\{.*?\}', definicao_formal)

            for i in range(len(def_formal_array)):
                def_formal_array[i] = def_formal_array[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

            self.variaveis = def_formal_array[0]
            self.terminais = def_formal_array[1]
            self.variavel_inical = def_formal_array[2][0]
            self.caracter_nulo = simbolo_vazio.strip()
            self.funcao_transicao = {}

            if self.caracter_nulo == '':
                messagebox.showinfo("GRUTIN", "O símbolo vazio não pode ser espaço em branco!")
            else:
                exists = False
                for terminal in self.terminais:
                    if self.caracter_nulo in terminal:
                        exists = True

                if not exists:
                    messagebox.showinfo("GRUTIN", "O símbolo vazio deve constar no conjunto de Terminais!")
                else:
                    self.cria_funcao_transicao()

    def cria_funcao_transicao(self):
        self.montar_tabela_funcao_transicao()
        self.table_funcao_transicao.cellChanged.connect(self.celula_atual())

    def montar_tabela_funcao_transicao(self):
        self.table_funcao_transicao.setColumnCount(len(self.variaveis))
        self.table_funcao_transicao.setRowCount(1)

        verticalHeaderLabels = ['Produções']

        self.table_funcao_transicao.setHorizontalHeaderLabels(self.variaveis)
        self.table_funcao_transicao.setVerticalHeaderLabels(verticalHeaderLabels)

        self.table_funcao_transicao.setEnabled(True)

    def celula_atual(self):
        linha = self.table_funcao_transicao.currentRow()
        coluna = self.table_funcao_transicao.currentColumn()
        valor = self.table_funcao_transicao.item(linha, coluna).text()

        if valor.strip() != '':
            valor = valor.replace(' ', '').split('|')

            for v in valor:
                var = self.variaveis[linha]
                if v != '':
                    self.funcao_transicao.add((var, v))

    def validar_glc(self):
        self.gramatica_livre_contexto = CFG(
            variables=set(self.variaveis),
            terminals=set(self.terminais),
            rules=self.funcao_transicao,
            start_variable=self.variavel_inical,
            null_character=self.caracter_nulo
        )

        self.btn_producoes_inuteis.setEnabled(True)
        self.btn_producoes_vazias.setEnabled(True)
        self.btn_fnc.setEnabled(True)
        self.txt_string_validacao.setEnabled(True)
        self.btn_validar_string.setEnabled(True)
        self.btn_validar_glc.setEnabled(True)

    def exec_producoes_inuteis(self):
        self.gramatica_livre_contexto.remove_unit_rules()
        self.set_txt_producoes_inuteis(self.gramatica_livre_contexto.str_rules(return_list=False))

    def exec_producoes_vazias(self):
        self.gramatica_livre_contexto.remove_null_rules()
        self.set_txt_producoes_vazias(self.gramatica_livre_contexto.str_rules(return_list=False))

    def exec_forma_normal_chomsky(self):
        self.gramatica_livre_contexto.chamsky()
        self.set_txt_fnc(self.gramatica_livre_contexto.str_rules(return_list=False))

    def valida_string(self, cadeia_glc):
        cadeia_aceita = self.gramatica_livre_contexto.cyk(cadeia_glc)

        if cadeia_aceita:
            messagebox.showinfo("GRUTIN", "Gramática Aceita pela GLC")
        else:
            messagebox.showinfo("GRUTIN", "Gramática não Aceita pela GLC")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gramática Livre de Contexto"))
        self.btn_valida_def_formal.setText(_translate("Form", "Validar Definição Formal"))
        self.btn_producoes_vazias.setText(_translate("Form", "Produções Vazias/Unitárias"))
        self.btn_producoes_inuteis.setText(_translate("Form", "Produções Inúteis"))
        self.btn_fnc.setText(_translate("Form", "Forma Normal de Chomsky"))
        self.btn_validar_string.setText(_translate("Form", "Validar String"))
        self.lbl_simbolo_vazio.setText(_translate("Form", "Símbolo vazio:"))
        self.lb_producoes_vazias.setText(_translate("Form", "Eliminar Produções Vazias/Unitárias:"))
        self.lbl_producoes_inuteis.setText(_translate("Form", "Eliminar Produções Inúteis:"))
        self.lbl_fnc.setText(_translate("Form", "Forma Normal de Chomsky:"))
        self.btn_validar_glc.setText(_translate("Form", "Validar Gramática Livre de Contexto"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GLCScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
