from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(150,150,365,300)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()
        
        self.tabela = QTableWidget()
        self.tabela.setRowCount(10)
        self.tabela.setColumnCount(5)

        botao0 = QPushButton('SAIR', self)
        #botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)

        layout.addWidget(self.tabela)
        layout.addWidget(botao0)

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