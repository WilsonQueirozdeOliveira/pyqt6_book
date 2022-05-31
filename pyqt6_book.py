import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema')
        self.setWindowIcon(QIcon('logo_wilson_eletrica.jpg'))
        self.setGeometry(150, 80, 1000, 600)
        self.Interface()

        self.show()

    def Interface(self):
        self.fundo = QLabel(self)
        self.fundo.setPixmap(QPixmap('background.jpg'))
        
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('logo_wilson_eletrica.jpg'))
        self.img.move(200,200)
        self.img.resize(200,200)
        
        botao1 = QPushButton('SAIR', self)
        botao1.resize(100,50)
        botao1.move(800,500)
        botao1.clicked.connect(self.sair)
        
        botao2 = QPushButton('MAIUSCULO', self)
        botao2.resize(100,25)
        botao2.move(5,50)
        botao2.clicked.connect(self.maiusculo)
        
        botao3 = QPushButton('minusculo', self)
        botao3.resize(100,25)
        botao3.move(110,50)
        botao3.clicked.connect(self.minusculo)
        
        botao4 = QPushButton('Entrar', self)
        botao4.resize(100,25)
        botao4.move(50,185)
        botao4.clicked.connect(self.salva_dados)
        
        texto1 = QLabel('Hello World!!!', self)
        texto1.resize(100,25)
        texto1.move(5,2)

        self.texto2 = QLabel('Wilson Queiroz!!!', self)
        self.texto2.resize(125,25)
        self.texto2.move(5,25)
        
        texto3 = QLabel('Login', self)
        texto3.resize(100,25)
        texto3.move(25,100)
        
        texto4 = QLabel('Senha', self)
        texto4.resize(100,25)
        texto4.move(25,130)
        
        self.caixa_texto1 = QLineEdit(self)
        self.caixa_texto1.setPlaceholderText('usuário')
        self.caixa_texto1.resize(100,25)
        self.caixa_texto1.move(75,100)
                
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('senha')
        self.caixa_texto2.setEchoMode(QLineEdit.EchoMode.Password)
        self.caixa_texto2.resize(100,25)
        self.caixa_texto2.move(75,130)
        
        self.salvar_checkbox = QCheckBox('Salvar informações', self)
        self.salvar_checkbox.move(90,160)
        self.salvar_checkbox.clicked.connect(self.salva_dados)
        
    def sair(self):
        sys.exit(qt.exec())
        
    def maiusculo(self):
        self.texto2.setText('WILSON QUEIROZ!!!')
        self.texto2.resize(300,25)
        self.texto2.move(5,25)
        
    def minusculo(self):
        self.texto2.setText('wilson queiroz!!!')
        self.texto2.resize(125,25)
        self.texto2.move(5,25)
        
    def salva_dados(self):
        base = []
        base.append(self.caixa_texto1.text())
        base.append(self.caixa_texto2.text())
        print(base)
        
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())