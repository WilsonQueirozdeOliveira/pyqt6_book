from ast import arguments
from re import S
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icone.png'))
        self.initUI()

    def initUI(self):
        barra_menu = self.menuBar()
        menu_arquivo = barra_menu.addMenu('Arquivo')

        menu_principal = QMenu('Categoria Principal', self)
        sub_menu_1 = QAction('Sub Categoria 1', self)
        sub_menu_2 = QAction('Sub Categoria 2', self)
        menu_principal.addAction(sub_menu_1)
        menu_principal.addAction(sub_menu_2)
        menu_1 = QAction('Opção Comum', self)
        menu_arquivo.addAction(menu_1)
        menu_arquivo.addMenu(menu_principal)
        
        botao0 = QPushButton('SAIR', self)
        botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)

        self.setGeometry(150,150,365,300)
        self.setWindowTitle('Menus e submenus')
        #self.Interface()


        self.show()
        
    def Interface(self):
        pass
     
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
                                         "Are you sure want to stop process?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())