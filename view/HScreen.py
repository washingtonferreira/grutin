# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from view.AFDScreen import Ui_AFDScreen
from view.AFNDScreen import Ui_AFNDScreen
from view.DPDAScreen import Ui_DPDAScreen
from view.GLCScreen import Ui_GLCScreen
from view.MTScreen import Ui_MTScreen


class Ui_MainWindow(object):
    def openAFDScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AFDScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAFNDScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AFNDScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDPDAScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DPDAScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMTScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MTScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def openGLCScrenn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GLCScreen();
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 266)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 551, 241))
        self.label.setObjectName("label")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName("menubar")

        self.menu_automatos = QtWidgets.QMenu(self.menubar)
        self.menu_automatos.setObjectName("menu_automatos")

        self.menuAFD = QtWidgets.QMenu(self.menu_automatos)
        self.menuAFD.setObjectName("menuAFD")

        self.menuAFND = QtWidgets.QMenu(self.menu_automatos)
        self.menuAFND.setObjectName("menuAFND")

        self.menuPDA = QtWidgets.QMenu(self.menu_automatos)
        self.menuPDA.setObjectName("menuPDA")

        self.menumaquina_de_turing = QtWidgets.QMenu(self.menubar)
        self.menumaquina_de_turing.setObjectName("menumaquina_de_turing")

        self.gramaticaLivreDeContexto = QtWidgets.QMenu(self.menubar)
        self.gramaticaLivreDeContexto.setObjectName("gramaticaLivreDeContexto")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionAutomato_2 = QtWidgets.QAction(MainWindow)
        self.actionAutomato_2.setObjectName("actionAutomato_2")
        self.actionAutomato_2.triggered.connect(self.callAFDScreen)

        self.actionExercicios_4 = QtWidgets.QAction(MainWindow)
        self.actionExercicios_4.setObjectName("actionExercicios_4")
        self.actionExercicios_4.triggered.connect(self.callExercise)

        self.actionAutomato_3 = QtWidgets.QAction(MainWindow)
        self.actionAutomato_3.setObjectName("actionAutomato_3")
        self.actionAutomato_3.triggered.connect(self.callAFNDScreen)

        self.actionExercicios_5 = QtWidgets.QAction(MainWindow)
        self.actionExercicios_5.setObjectName("actionExercicios_5")
        self.actionExercicios_5.triggered.connect(self.callExercise)

        self.actionAutomato_4 = QtWidgets.QAction(MainWindow)
        self.actionAutomato_4.setObjectName("actionAutomato_4")
        self.actionAutomato_4.triggered.connect(self.callPDAScreen)

        self.actionExercicios_6 = QtWidgets.QAction(MainWindow)
        self.actionExercicios_6.setObjectName("actionExercicios_6")

        self.menuAFD.addAction(self.actionAutomato_2)
        self.menuAFD.addAction(self.actionExercicios_4)

        self.menuAFND.addAction(self.actionAutomato_3)
        self.menuAFND.addAction(self.actionExercicios_5)

        self.menuPDA.addAction(self.actionAutomato_4)
        self.menuPDA.addAction(self.actionExercicios_6)

        self.actionMT = QtWidgets.QAction(MainWindow)
        self.actionMT.setObjectName("actionMT")
        self.actionMT.triggered.connect(self.callMT)
        # self.menu_automatos.addSeparator()

        self.actionGLC = QtWidgets.QAction(MainWindow)
        self.actionGLC.setObjectName("actionGLC")
        self.actionGLC.triggered.connect(self.callGLC)

        self.menu_automatos.addAction(self.menuAFD.menuAction())
        self.menu_automatos.addAction(self.menuAFND.menuAction())
        self.menu_automatos.addAction(self.menuPDA.menuAction())

        self.menumaquina_de_turing.addAction(self.actionMT)
        self.menubar.addAction(self.menu_automatos.menuAction())
        self.menubar.addAction(self.menumaquina_de_turing.menuAction())

        self.gramaticaLivreDeContexto.addAction(self.actionGLC)
        self.menubar.addAction(self.gramaticaLivreDeContexto.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def callGLC(self):
        self.openGLCScrenn()

    def callAFDScreen(self):
        self.openAFDScreen()

    def callAFNDScreen(self):
        self.openAFNDScreen()

    def callPDAScreen(self):
        self.openDPDAScreen()

    def callExercise(self):
        self.label.setText(
            '1 - Crie um automato que aceite a cadeia 001101 \n'
            '2 - Usando apenas 4 estados, crie um automato que aceite a cadeia 001110101 \n'
            '3 - Defina uma tabela de transição para o automato ({q0, q1, q2, q3}, {0,1}, d, {q0}, {q2})')

    def callMT(self):
        self.openMTScreen()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Principal"))
        self.label.setText(_translate("MainWindow", ""))
        self.menu_automatos.setTitle(_translate("MainWindow", "Autômatos"))
        self.menuAFD.setTitle(_translate("MainWindow", "AFD"))
        self.menuAFND.setTitle(_translate("MainWindow", "AFND"))
        self.menuPDA.setTitle(_translate("MainWindow", "PDA"))
        self.gramaticaLivreDeContexto.setTitle(_translate("MainWindow", "GLC"))
        self.menumaquina_de_turing.setTitle(_translate("MainWindow", "maquina de turing"))
        self.actionAutomato_2.setText(_translate("MainWindow", "Automato"))
        self.actionExercicios_4.setText(_translate("MainWindow", "Exercicios"))
        self.actionAutomato_3.setText(_translate("MainWindow", "Automato"))
        self.actionExercicios_5.setText(_translate("MainWindow", "Exercicios"))
        self.actionAutomato_4.setText(_translate("MainWindow", "Automato"))
        self.actionExercicios_6.setText(_translate("MainWindow", "Exercicios"))
        self.actionMT.setText(_translate("MainWindow", "MT"))
        self.actionGLC.setText(_translate("MainWindow", "GLC"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
