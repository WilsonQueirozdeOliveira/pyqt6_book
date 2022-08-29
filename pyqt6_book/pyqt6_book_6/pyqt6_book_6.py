from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150,150,365,300)

        self.central = QWidget()
        self.grid = QGridLayout(self.central)

        self.botao1 = QPushButton('Botão 1')
        self.grid.addWidget(self.botao1, 0, 0, 1, 1)

        self.botao2 = QPushButton('Botão 2')
        self.grid.addWidget(self.botao2, 1, 2, 1, 1)

        self.botao0 = QPushButton('SAIR')
        self.grid.addWidget(self.botao0, 2, 2, 1, 1)
        self.botao0.clicked.connect(self.confirma_saida)

        self.setCentralWidget(self.central)       
        
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