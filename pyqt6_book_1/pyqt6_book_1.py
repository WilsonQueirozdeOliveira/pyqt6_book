from ast import arguments
from re import S
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
        self.fundo.setPixmap(QPixmap('background_gray.jpg'))
        
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('python.png'))
        self.img.move(80,250)
        self.img.resize(200,200)
        
        botao1 = QPushButton('SAIR', self)
        botao1.resize(100,50)
        botao1.move(800,500)
        botao1.clicked.connect(self.confirma_saida)
        #botao1.clicked.connect(self.sair)
        
        botao2 = QPushButton('MAIUSCULO', self)
        botao2.resize(100,25)
        botao2.move(90,50)
        botao2.clicked.connect(self.maiusculo)
        
        botao3 = QPushButton('minusculo', self)
        botao3.resize(100,25)
        botao3.move(200,50)
        botao3.clicked.connect(self.minusculo)
        
        botao4 = QPushButton('Entrar', self)
        botao4.resize(100,25)
        botao4.move(90,500)
        botao4.clicked.connect(self.salva_dados)
        botao4.clicked.connect(self.sel_ambiente)
        botao4.clicked.connect(self.sel_tema)
        botao4.clicked.connect(self.envia_argumento)
        
        texto1 = QLabel('Hello World!!!', self)
        texto1.resize(100,25)
        texto1.move(90,2)

        self.texto2 = QLabel('Wilson Queiroz!!!', self)
        self.texto2.resize(125,25)
        self.texto2.move(90,25)
        
        texto3 = QLabel('Login', self)
        texto3.resize(100,25)
        texto3.move(35,100)
        
        texto4 = QLabel('Senha', self)
        texto4.resize(100,25)
        texto4.move(35,130)
        
        self.caixa_texto1 = QLineEdit(self)
        self.caixa_texto1.setPlaceholderText('usuário')
        self.caixa_texto1.resize(100,25)
        self.caixa_texto1.move(90,100)
                
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('senha')
        self.caixa_texto2.setEchoMode(QLineEdit.EchoMode.Password)
        self.caixa_texto2.resize(100,25)
        self.caixa_texto2.move(90,130)
        
        self.salvar_checkbox = QCheckBox('Salvar informações', self)
        self.salvar_checkbox.move(90,160)
        self.salvar_checkbox.clicked.connect(self.salva_dados)
        
        self.seleciona_ambiente = QComboBox(self)
        self.seleciona_ambiente.move(90, 185)
        #self.seleciona_ambiente.addItem('Ambiente Comum')
        #self.seleciona_ambiente.addItem('Painel de controle')
        self.seleciona_ambiente.addItems(['Ambiente Comum',
                                          'Painel de controle'])
        
        self.seleciona_tema1 = QRadioButton('Tema Claro', self)
        self.seleciona_tema1.move(90,215)
        self.seleciona_tema1.setChecked(True)
        self.seleciona_tema2 = QRadioButton('Tema Escuro', self)
        self.seleciona_tema2.move(170,215)

        botao_sobre = QPushButton('Sobre', self)
        botao_sobre.move(800,50)
        botao_sobre.clicked.connect(self.sobre)

        self.tamanho_fonte = QSpinBox(self)
        self.tamanho_fonte.move(520,297)
        texto_tamanho_fonte = QLabel('Tamanho da Fonte:', self)
        texto_tamanho_fonte.move(405,300)
        self.tamanho_fonte.setMinimum(100)
        self.tamanho_fonte.setMaximum(150)
        self.tamanho_fonte.setSuffix('%')
        self.tamanho_fonte.setSingleStep(10)
        self.tamanho_fonte.valueChanged.connect(self.tam_fonte)

        self.texto = QTextEdit(self)
        self.texto.setFixedWidth(280)
        self.texto.setFixedHeight(40)
        self.texto.move(250,158)
        argumentos = QLabel('Insira suas observações abaixo:', self)
        argumentos.move(250,143)
        self.texto_checkbox = QCheckBox('Salvar observações', self)
        self.texto_checkbox.move(250, 198)

        
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
        if self.salvar_checkbox.isChecked():
            base = []
            base.append(self.caixa_texto1.text())
            base.append(self.caixa_texto2.text())
            #print(base)
            print(f'Nome do usuário: {base[0]}, Senha: {base[1]}')
        else:
            print(f'Usuário optou por não salvar os dados.')
                
    def sel_ambiente(self):
        ambiente_selecionado = self.seleciona_ambiente.currentText()
        print(f'O ambiente escolhido é: {ambiente_selecionado}')
        
    def sel_tema(self):
        if self.seleciona_tema1.isChecked():
            print(f'Tema Claro Escolhido')
        else:
            print(f'Tema Escuro Escolhido')

    def confirma_saida(self):
        #confirma = QMessageBox.question(self,
        confirma = QMessageBox.critical(self,
                                        'Atenção',
                                        'Deseja mesmo sair?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if confirma == QMessageBox.StandardButton.Yes:
            sys.exit(qt.exec())
        if confirma == QMessageBox.StandardButton.Cancel:
            pass

    def sobre(self):
        sobre = QMessageBox.information(self,'Meu Programa','Versão 1.0.0')

    def tam_fonte(self):
        valor = self.tamanho_fonte.value()
        fonte0 = QFont('Times',10)
        fonte1 = QFont('Times',11)
        fonte2 = QFont('Times',12)
        fonte3 = QFont('Times',13)
        fonte4 = QFont('Times',14)
        fonte5 = QFont('Times',15)
        if valor == 110:
            self.caixa_texto1.setFont(fonte1)
            self.caixa_texto2.setFont(fonte1)
        elif valor == 120:
            self.caixa_texto1.setFont(fonte2)
            self.caixa_texto2.setFont(fonte2)
        elif valor == 130:
            self.caixa_texto1.setFont(fonte3)
            self.caixa_texto2.setFont(fonte3)
        elif valor == 140:
            self.caixa_texto1.setFont(fonte4)
            self.caixa_texto2.setFont(fonte4)
        elif valor == 150:
            self.caixa_texto1.setFont(fonte5)
            self.caixa_texto2.setFont(fonte5)
        else:
            self.caixa_texto1.setFont(fonte0)
            self.caixa_texto2.setFont(fonte0)
        
    def envia_argumento(self):
        if self.texto_checkbox.isChecked():
            observacoes = []
            observacoes.append(self.texto.toPlainText())
            print('Observações salvas com sucesso.')
            print(f'{observacoes}')
        else:
            print('O usuário não inseriu nenhuma observação.')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
