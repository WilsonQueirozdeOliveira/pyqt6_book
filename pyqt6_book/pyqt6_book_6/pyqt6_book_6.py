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
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.botao1 = QPushButton('Botão 1')
        self.botao1.clicked.connect(self.botao_funcao1)
        self.grid.addWidget(self.botao1, 1, 1, 2, 1)
        #self.grid.addWidget(widget,linha,coluna,
        # espansão da linha,espansão da coluna)

        self.botao2 = QPushButton('Botão 2')
        self.grid.addWidget(self.botao2, 2, 2, 8, 1)

        self.botao3 = QPushButton('Botão 3')
        self.grid.addWidget(self.botao3, 2, 1, 8,1)

        self.botao0 = QPushButton('SAIR')
        self.grid.addWidget(self.botao0, 3, 2, 13, 1)
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

    def botao_funcao1(self):
        pass
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())