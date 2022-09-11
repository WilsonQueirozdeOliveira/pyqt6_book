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
        self.Interface()
        
    def Interface(self):
        barra_menu = self.menuBar()

        menu_arquivo = barra_menu.addMenu('Arquivo')
        menu_config = barra_menu.addMenu('Configuração')
        menu_ajuda = barra_menu.addMenu('Ajuda')

        menu_arquivo_sub_novo = QAction('Novo Projeto', self)
        menu_arquivo_sub_novo.setIcon((QIcon('icone.png')))
        menu_arquivo.addAction(menu_arquivo_sub_novo)
        menu_arquivo_sub_novo.setShortcut('Ctrl+N')
        menu_arquivo_sub_novo.triggered.connect(self.novo)
        menu_arquivo_sub_abrir = QAction('Abrir Projeto', self)
        menu_arquivo.addAction(menu_arquivo_sub_abrir)
        menu_config_sub_interface = QAction('Interface', self)
        menu_config.addAction(menu_config_sub_interface)
        menu_arquivo_sub_sair = QAction('Sair', self)
        menu_arquivo.addAction(menu_arquivo_sub_sair)
        menu_arquivo_sub_sair.triggered.connect(self.confirma_saida)

        botao0 = QPushButton('SAIR', self)
        botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)

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