from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu programa')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150,150,350,300)
        self.Interface()
        
    def Interface(self):
        layout = QFormLayout()

        texto_usuario = QLabel('Usuário:')
        texto_usuario.move(275,260)
        input_usuario = QLineEdit()
        input_usuario.setPlaceholderText('Digite seu nome de usuário')
        texto_senha = QLabel('Senha:')
        input_senha = QLineEdit()
        input_senha.setPlaceholderText('Digite sua senha')
        input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        seleciona_ambiente = QComboBox()
        seleciona_ambiente.addItem('Ambiente Comum')
        seleciona_ambiente.addItem('Painel de controle')

        botao0 = QPushButton('SAIR', self)
        #botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)

        layout.addRow(texto_usuario, input_usuario)
        layout.addRow(texto_senha,input_senha)
        layout.addRow(QLabel('Salvar Informações:'), seleciona_ambiente)
        
        layout_secundario = QHBoxLayout()
        layout_secundario.addStretch()
        layout_secundario.addWidget(QPushButton('Entrar'))
        layout_secundario.addWidget(botao0)
        layout_secundario.addStretch()
        layout.addRow(layout_secundario)

        self.setLayout(layout)

        self.show()

    def confirma_saida(self):
        confirma = QMessageBox.question(self,
        #confirma = QMessageBox.critical(self,
                                        'Atenção',
                                        'Deseja mesmo sair?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if confirma == QMessageBox.StandardButton.Yes:
            print('exit comfirmed')
            sys.exit(qt.exec())
        if confirma == QMessageBox.StandardButton.Cancel:
            print('exit not comfirmed')
            pass
        pass
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())