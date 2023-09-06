import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_ComputerIcon')
        icon = self.style().standardIcon(pixmapi)
        #barra_ferramentas_botao_novo.setIcon(icon)
        #self.setWindowIcon(QIcon('icone.png'))
        self.setWindowIcon(icon)
        self.setGeometry(0,0,1000,800)
        self.Interface()

    def Interface(self):
        barra_menu = self.menuBar()

        '''
        menu_arquivo = barra_menu.addMenu('Arquivo')
        
        menu_arquivo_sub_novo = QAction('Novo Projeto', self)
        menu_arquivo_sub_novo.setIcon((QIcon('icone.png')))
        menu_arquivo.addAction(menu_arquivo_sub_novo)
        menu_arquivo_sub_novo.setShortcut('Ctrl+N')
        menu_arquivo_sub_novo.triggered.connect(self.novo)

        menu_arquivo_sub_abrir = QAction('Abrir Projeto', self)
        menu_arquivo.addAction(menu_arquivo_sub_abrir)

        menu_arquivo_sub_sair = QAction('Sair', self)
        menu_arquivo.addAction(menu_arquivo_sub_sair)
        menu_arquivo_sub_sair.triggered.connect(self.confirma_saida)
        '''

        menu_calcular = barra_menu.addMenu('Calcular')
        menu_calcular_sub_configuracao_de_maquina = QAction('Configuração de Máquina', self)
        menu_calcular.addAction(menu_calcular_sub_configuracao_de_maquina)
        menu_calcular_sub_configuracao_de_maquina.triggered.connect(self.show_layout_configuracao_de_maquina)        
        menu_calcular_sub_velocidade_e_carga_de_eixo = QAction('velocidade e Carga no Eixo', self)
        menu_calcular.addAction(menu_calcular_sub_velocidade_e_carga_de_eixo)
        menu_calcular_sub_velocidade_e_carga_de_eixo.triggered.connect(self.show_layout_velocidade_e_carga_no_eixo)
        menu_calcular_sub_veliculo_eletrico = QAction('Veículo Elétrico', self)
        menu_calcular.addAction(menu_calcular_sub_veliculo_eletrico)
        menu_calcular_sub_veliculo_eletrico.triggered.connect(self.novo)

        menu_ajuda = barra_menu.addMenu('sobre')
        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        barra_ferramentas_botao_novo = QAction('Novo',self)#SP_FileIcon
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_FileIcon')
        icon = self.style().standardIcon(pixmapi)
        barra_ferramentas_botao_novo.setIcon(icon)
        barra_ferramentas_botao_novo.triggered.connect(self.novo)
        #barra_ferramentas.addAction(barra_ferramentas_botao_novo)

        barra_ferramentas_botao_gerar_pdf = QAction('Gerar PDF',self)#SP_FileDialogDetailedView
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_FileDialogDetailedView')
        icon = self.style().standardIcon(pixmapi)
        barra_ferramentas_botao_gerar_pdf.setIcon(icon)
        barra_ferramentas_botao_gerar_pdf.triggered.connect(self.gerar_pdf)
        barra_ferramentas.addAction(barra_ferramentas_botao_gerar_pdf)

        barra_ferramentas_botao_sair = QAction(QIcon('icone.png'),'Sair',self)#SP_TitleBarCloseButton
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_TitleBarCloseButton')
        icon = self.style().standardIcon(pixmapi)
        barra_ferramentas_botao_sair.setIcon(icon)
        barra_ferramentas_botao_sair.triggered.connect(self.confirma_saida)
        barra_ferramentas.addAction(barra_ferramentas_botao_sair)

        self.main_widget = QWidget()
        self.scroll = QScrollArea()
        self.layout_principal = QGridLayout()

        for row in range (10):
            self.layout_principal.setRowMinimumHeight(row,25)
        for colunm in range (2):
            self.layout_principal.setColumnMinimumWidth(colunm,300)

        #### layouts ####
        '''
        self.inicio_grid = QGridLayout()
        for row in range (10):
            self.inicio_grid.setRowMinimumHeight(row,30)
        for colunm in range (10):
            self.inicio_grid.setColumnMinimumWidth(colunm,70)

        tipo_de_maquina = QLabel('Qual o tipo de máquina?')
        tipo_de_maquina.setFixedSize(225, 22)

        self.input_tipo_de_maquina = QComboBox(self)
        self.input_tipo_de_maquina.setFixedHeight(22)
        self.input_tipo_de_maquina.setPlaceholderText('nenhum')
        self.input_tipo_de_maquina.addItems(['nenhum',
                                            'esteira',
                                            'separador',
                                            'enchedora',
                                            'especial'])
        self.input_tipo_de_maquina.currentIndexChanged.connect(self.atualizar_layout)

        #botao_0 = QPushButton('teste 0 (0,2)', self)
        #botao_1 = QPushButton('teste 1 (0,3)', self)
        botao_3 = QPushButton('teste 3 (10,10)', self)
        botao_3.setFixedHeight(22)

        self.statusBar().showMessage('Programa inicializado corretamente...')

        self.inicio_grid.addWidget(tipo_de_maquina,0,0,)
        self.inicio_grid.addWidget(self.input_tipo_de_maquina,0,1)
        #self.inicio_grid.addWidget(botao_0,0,2)
        #self.inicio_grid.addWidget(botao_1,0,3)
        self.inicio_grid.addWidget(botao_3,10,10)
        
        self.main_widget.setLayout(self.inicio_grid)
        '''
        '''
        self.teste_widget = QLabel('teste widget')
        self.teste_widget.setMinimumHeight(20)
        self.layout_principal.addWidget(self.teste_widget,0,0,Qt.AlignmentFlag.AlignTop)
        '''
        
        self.main_widget.setLayout(self.layout_principal)

        self.scroll.setWidget(self.main_widget)

        self.setCentralWidget(self.scroll)

        self.show()
    '''
    def atualizar_layout(self):
        print('atualizar layout')
        if self.input_tipo_de_maquina.currentText() == 'esteira':
            print('novo widget')
            self.modelo_da_maquina = QLabel('Qual o modelo da máquina?')
            self.modelo_da_maquina.setFixedSize(250, 22)
            self.inicio_grid.addWidget(self.modelo_da_maquina,1,0)
        elif self.input_tipo_de_maquina.currentText() == 'nenhum':
            self.inicio_grid.removeWidget(self.modelo_da_maquina)
            self.modelo_da_maquina.deleteLater()
            self.modelo_da_maquina = None
    '''

    def show_layout_configuracao_de_maquina(self):
        
        print('layout_configuracao_de_maquina')
        try:
            for i in reversed(range(self.layout_principal.count())): 
                self.layout_principal.itemAt(i).widget().setParent(None)
        except:
            print('widgets no layout_principal nao existe ainda')
        
        self.layout_configuracao_de_maquina = QGridLayout()
        for row in range (10):
            self.layout_configuracao_de_maquina.setRowMinimumHeight(row,30)

        self.configuracao_de_maquina = QLabel('Configuração de Máquina') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        self.tipo_de_maquina = QLabel('Qual o tipo de máquina?') 
        self.modelo_da_maquina = QLabel('Qual o modelo da máquina?')
        
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)
        self.layout_principal.addWidget(self.tipo_de_maquina,1,0,Qt.AlignmentFlag.AlignTop)
        self.layout_principal.addWidget(self.modelo_da_maquina,2,0,Qt.AlignmentFlag.AlignTop)
        

    def show_layout_velocidade_e_carga_no_eixo(self):
        print('show_layout_velocidade_e_carga_no_eixo')

        try:
            for i in reversed(range(self.layout_principal.count())): 
                self.layout_principal.itemAt(i).widget().setParent(None)
        except:
            print('widgets no layout_principal nao existe ainda')

        self.layout_velocidade_e_carga_no_eixo = QGridLayout()
        for row in range (10):
            self.layout_velocidade_e_carga_no_eixo.setRowMinimumHeight(row,30)

        self.configuracao_de_maquina = QLabel('velocidade_e_carga_no_eixo') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)
        pass
        

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
app.setStyleSheet('.QLabel { font-size: 14pt;} .QLineEdit { font-size: 14pt;}')
sys.exit(qt.exec())