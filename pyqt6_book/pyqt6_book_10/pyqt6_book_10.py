from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QWidget):# widget/estrutura da janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150,150,365,300)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()# widget/layout interno da janela 

        self.abas = QTabWidget()#widget/Estrutura de abas
        
        self.aba1 = QWidget()
        self.abas.addTab(self.aba1, 'Principal')

        self.aba2 = QWidget()
        self.abas.addTab(self.aba2, 'inventário')

        self.aba3 = QWidget()
        self.abas.addTab(self.aba3, 'sobre')

        layout.addWidget(self.abas)

        #conteudo aba1--------------------
        layout_aba1 = QVBoxLayout()#layout interno da primeira aba1
        layout_aba1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto_a1 = QLabel('Seja muito bem vindo(a)!!!')
        self.texto_a2 = QLabel('Para acessar o inventário, clique sobre a aba Inventário...')
        self.texto_a3 = QLabel('Para fechar o programa clique no botao SAIR')
        
        self.botao0 = QPushButton('SAIR', self)
        #botao0.move(275,260)
        self.botao0.clicked.connect(self.confirma_saida)

        layout_aba1.addWidget(self.texto_a1)
        layout_aba1.addWidget(self.texto_a2)
        layout_aba1.addWidget(self.texto_a3)

        layout_aba1.addWidget(self.botao0)
        self.aba1.setLayout(layout_aba1)
        #layout.addWidget(botao0)
        #conteudo aba1----------------------

        #conteudo aba2----------------------
        layout_aba2 = QVBoxLayout()
        self.tabela = QTableWidget()
        self.tabela.setRowCount(10)
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderItem(0, QTableWidgetItem('Item'))
        self.tabela.setHorizontalHeaderItem(1, QTableWidgetItem('Quantidade'))
        self.tabela.setHorizontalHeaderItem(2, QTableWidgetItem('Valor'))
        layout_aba2.addWidget(self.tabela)
        self.aba2.setLayout(layout_aba2)
        #conteudo aba2----------------------

        #conteudo aba3----------------------
        layout_aba3 = QVBoxLayout()
        layout_aba3.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.texto_a3 = QLabel('2022 - Wilson Queiroz, Todos os Diritos Reservados')
        layout_aba3.addWidget(self.texto_a3)
        self.aba3.setLayout(layout_aba3)
        #conteudo aba3----------------------

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