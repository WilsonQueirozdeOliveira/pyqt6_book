from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150,150,365,300)
        self.Interface()

        self.show()

    def Interface(self):
        self.texto1 = QLabel(
        'Insira no campo abaixo o dado/valor: ',self)
        self.texto1.move(10, 33)
        self.adiciona_cliente = QLineEdit(self)
        self.adiciona_cliente.setFixedWidth(255)
        self.adiciona_cliente.move(10,50)

        self.lista = QListWidget(self)
        self.lista.move(10, 80)

        botao_adiciona = QPushButton('Adicionar',self)
        botao_adiciona.move(270, 80)
        botao_adiciona.clicked.connect(self.adiciona_elemento)
        botao_selecionar = QPushButton('Selecionar', self)
        botao_selecionar.move(270, 110)
        botao_selecionar.clicked.connect(self.seleciona_elemento)
        botao_remover = QPushButton('Remover', self)
        botao_remover.move(270,140)
        botao_remover.clicked.connect(self.remove_elemento)
        botao_remover_tudo = QPushButton('Remover Tudo', self)
        botao_remover_tudo.move(270,170)
        botao_remover_tudo.clicked.connect(self.remove_tudo)

        botao1 = QPushButton('SAIR', self)
        botao1.move(275,260)
        botao1.clicked.connect(self.confirma_saida)

    def adiciona_elemento(self):
        elemento = []
        elemento.append(self.adiciona_cliente.text())
        print(elemento)
        self.lista.addItem(elemento[0])
        self.adiciona_cliente.setText(elemento[0])
        pass

    def seleciona_elemento(self):
        elemento = []
        if self.lista.currentItem():
            elemento = self.lista.currentItem().text()
            print(elemento)
        else:
            print('no item on list / or no item selected')
        pass

    def remove_elemento(self):
        indice = []
        indice = self.lista.currentRow()
        print(indice)
        self.lista.takeItem(indice)
        pass

    def remove_tudo():
        pass

    def confirma_saida():
        pass

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())