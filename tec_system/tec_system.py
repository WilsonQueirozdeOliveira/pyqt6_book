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
        self.setGeometry(150,150,400,320)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()

        self.abas = QTabWidget()

        self.aba1 = QWidget()
        self.abas.addTab(self.aba1, 'Configurar máquina')
        layout_aba1 = QHBoxLayout()

        self.aba2 = QWidget()
        self.abas.addTab(self.aba2, 'Cálculos de transporte')
        layout_aba2 = QHBoxLayout()

        self.aba3 = QWidget()
        self.abas.addTab(self.aba3, 'sobre')
        layout_aba3 = QHBoxLayout()

        layout.addWidget(self.abas)

        self.aba1.setLayout(layout_aba1)
        self.aba2.setLayout(layout_aba2)
        self.aba3.setLayout(layout_aba3)

        botao0 = QPushButton('SAIR', self)
        #botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)

        layout_botoes_inferiores = QHBoxLayout()
        
        layout.addLayout(layout_botoes_inferiores)

        layout_botoes_inferiores.addStretch()
        layout_botoes_inferiores.addWidget(botao0)

        self.setLayout(layout)

        self.show()

    def novo(self):
        print('Novo projeto criado com sucesso.')

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

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                         "QUIT",
                                         "Are you sure want to stop the process?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())