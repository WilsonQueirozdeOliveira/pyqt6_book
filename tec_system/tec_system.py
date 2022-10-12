
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
        self.setGeometry(150,150,400,120)
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

        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        barra_ferramentas_botao_novo = QAction(QIcon('icone.png'),'Novo',self)
        barra_ferramentas_botao_novo.triggered.connect(self.novo)
        barra_ferramentas.addAction(barra_ferramentas_botao_novo)

        barra_ferramentas_botao_gerar_pdf = QAction(QIcon('icone.png'),'Gerar PDF',self)
        barra_ferramentas_botao_gerar_pdf.triggered.connect(self.gerar_pdf)
        barra_ferramentas.addAction(barra_ferramentas_botao_gerar_pdf)

        barra_ferramentas_botao_sair = QAction(QIcon('icone.png'),'Sair',self)
        barra_ferramentas_botao_sair.triggered.connect(self.confirma_saida)
        barra_ferramentas.addAction(barra_ferramentas_botao_sair)

        self.main_widget = QWidget()
        self.scroll = QScrollArea()
        self.inicio_grid = QGridLayout()

        botao_0 = QPushButton('0', self)
        botao_1 = QPushButton('1', self)
        botao_3 = QPushButton('3', self)

        self.statusBar().showMessage('Programa inicializado corretamente...')

        self.inicio_grid.addWidget(botao_0,0,0)
        self.inicio_grid.addWidget(botao_1,0,1)
        self.inicio_grid.addWidget(botao_3,10,10)
        
        self.main_widget.setLayout(self.inicio_grid)

        self.scroll.setWidget(self.main_widget)

        self.setCentralWidget(self.scroll)

        self.show()

    def novo(self):
        print('Novo projeto criado com sucesso.')

    def gerar_pdf(self):
        print('gerar pdf')

    def confirma_saida(self):
        confirma = QMessageBox.question(self,
        #confirma = QMessageBox.critical(self,
                                        'Atenção',
                                        'Deseja mesmo sair?     Dados não salvos serão perdidos!',
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
                                         "Encerrar processo",
                                         "Quer mesmo encerrar o processo?   Dados não salvos serão perdidos!",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())