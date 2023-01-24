import locale
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtWidgets

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Clientes')
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_ComputerIcon')
        icon = self.style().standardIcon(pixmapi)
        #barra_ferramentas_botao_novo.setIcon(icon)
        #self.setWindowIcon(QIcon('icone.png'))
        self.setWindowIcon(icon)
        self.setGeometry(700,40,1200,800)
        self.Interface()

    def Interface(self):
        barra_menu = self.menuBar()

        menu_arquivo = barra_menu.addMenu('Arquivo')
        
        menu_arquivo_sub_novo = QAction('Novo Projeto', self)
        menu_arquivo_sub_novo.setIcon((QIcon('icone.png')))
        menu_arquivo.addAction(menu_arquivo_sub_novo)
        menu_arquivo_sub_novo.setShortcut('Ctrl+N')
        menu_arquivo_sub_novo.triggered.connect(self.novo)
        '''
        menu_arquivo_sub_abrir = QAction('Abrir Projeto', self)
        menu_arquivo.addAction(menu_arquivo_sub_abrir)
        '''
        menu_arquivo_sub_sair = QAction('Sair', self)
        menu_arquivo.addAction(menu_arquivo_sub_sair)
        menu_arquivo_sub_sair.triggered.connect(self.confirma_saida)
        
        menu_calcular = barra_menu.addMenu('Calcular')
        menu_calcular_sub_configuracao_de_maquina = QAction('Configuração de Máquina', self)
        menu_calcular.addAction(menu_calcular_sub_configuracao_de_maquina)
        menu_calcular_sub_configuracao_de_maquina.triggered.connect(self.show_layout_configuracao_de_maquina)        
        menu_calcular_sub_velocidade_e_carga_de_eixo = QAction('velocidade e Carga no Eixo', self)
        menu_calcular.addAction(menu_calcular_sub_velocidade_e_carga_de_eixo)
        menu_calcular_sub_velocidade_e_carga_de_eixo.triggered.connect(self.show_layout_velocidade_e_carga_no_eixo)
        '''
        menu_calcular_sub_veliculo_eletrico = QAction('Veículo Elétrico', self)
        menu_calcular.addAction(menu_calcular_sub_veliculo_eletrico)
        menu_calcular_sub_veliculo_eletrico.triggered.connect(self.novo)
        '''
        #menu_ajuda = barra_menu.addMenu('ajuda')

        menu_sobre = barra_menu.addMenu('sobre')

        # Barra de ferramentas
        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        barra_ferramentas_botao_novo = QAction('Novo',self)#SP_FileIcon
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_FileIcon')
        icon = self.style().standardIcon(pixmapi)
        barra_ferramentas_botao_novo.setIcon(icon)
        barra_ferramentas_botao_novo.triggered.connect(self.novo)
        barra_ferramentas.addAction(barra_ferramentas_botao_novo)

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

        # layout
        self.main_widget = QWidget()
        self.scroll = QScrollArea()
        self.layout_principal = QGridLayout()

        for row in range (10):
            self.layout_principal.setRowMinimumHeight(row,30)
        for colunm in range (2):
            self.layout_principal.setColumnMinimumWidth(colunm,500)
        #self.layout_principal.columnStretch(0)
        
        self.main_widget.setLayout(self.layout_principal)

        self.scroll.setWidget(self.main_widget)

        self.setCentralWidget(self.scroll)

        self.show()
        localizacao = locale.setlocale(locale.LC_ALL,'')
        self.statusBar().showMessage('Programa inicializado corretamente...'+localizacao)
    

    def show_layout_configuracao_de_maquina(self):
        self.novo()

        self.titulo = ''
        self.titulo_da_maquina = QLabel('Titulo da Máquina: '+self.titulo)
        self.titulo_da_maquina.setStyleSheet("QLabel { color : black; font-weight: bold; }")
        self.layout_principal.addWidget(self.titulo_da_maquina,1,0,Qt.AlignmentFlag.AlignTop)

        print('show_layout_configuracao_de_maquina')
        self.statusBar().showMessage('show_layout_configuracao_de_maquina')

        self.configuracao_de_maquina = QLabel('Configuração de Máquina') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)

        self.tipo_de_maquina = QLabel('Qual o tipo de máquina?')
        self.layout_principal.addWidget(self.tipo_de_maquina,2,0,Qt.AlignmentFlag.AlignTop)

        self.input_tipo_de_maquina = QComboBox(self)
        self.input_tipo_de_maquina.setFixedHeight(22)
        self.input_tipo_de_maquina.setPlaceholderText('nenhum')
        self.input_tipo_de_maquina.addItems(['nenhum',
                                            'esteira',
                                            'separador',
                                            'enchedora',
                                            'especial'])
        
        self.input_tipo_de_maquina.currentIndexChanged.connect(self.tipo_de_maquina_definido)
        self.layout_principal.addWidget(self.input_tipo_de_maquina,2,1)

    def tipo_de_maquina_definido(self):
        self.data_input_tipo_de_maquina = self.input_tipo_de_maquina.currentText()
        print('self.data_input_tipo_de_maquina: '+self.data_input_tipo_de_maquina)
        print()
        if self.data_input_tipo_de_maquina == 'esteira':
            self.show_modelo_da_esteira()

        elif self.data_input_tipo_de_maquina == 'separador':
            self.show_modelo_do_separador()
            
        elif self.data_input_tipo_de_maquina == 'nenhum':
            self.esconha_tipo_de_maquina = QLabel('Escolha o tipo de máquina...')
            self.layout_principal.addWidget(self.esconha_tipo_de_maquina,3,0,Qt.AlignmentFlag.AlignTop)

    def show_modelo_da_esteira(self):        
        self.novo()

        self.titulo = ''+self.data_input_tipo_de_maquina
        self.titulo_da_maquina = QLabel('Titulo da Máquina: '+self.titulo)
        self.titulo_da_maquina.setStyleSheet("QLabel { color : black; font-weight: bold; }")
        self.layout_principal.addWidget(self.titulo_da_maquina,1,0,Qt.AlignmentFlag.AlignTop)

        self.configuracao_de_maquina = QLabel('Configuração de Máquina') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)
        
        if self.data_input_tipo_de_maquina == 'esteira':
            print('-> show_modelo_da_esteira')
            self.modelo_da_esteira = QLabel('Qual o modelo da esteira?')
            self.layout_principal.addWidget(self.modelo_da_esteira,2,0,Qt.AlignmentFlag.AlignTop)

            self.input_modelo_da_esteira = QComboBox(self)
            self.input_modelo_da_esteira.setFixedHeight(22)
            self.input_modelo_da_esteira.setPlaceholderText('nenhum')
            self.input_modelo_da_esteira.addItems(['nenhum',
                                            'ultraline',
                                            'premier',
                                            'classic',
                                            'super classic'])
                                            
            self.input_modelo_da_esteira.currentIndexChanged.connect(self.show_configuracao_da_esteira)
            self.layout_principal.addWidget(self.input_modelo_da_esteira,2,1)
            print('show_modelo_da_esteira ->')

    def show_modelo_do_separador(self):
        self.novo()            
        self.modelo_do_separador = QLabel('Configuraçao de separador não existente.')
        self.layout_principal.addWidget(self.modelo_do_separador,2,0,Qt.AlignmentFlag.AlignTop)

    def show_configuracao_da_esteira(self):
        self.data_input_modelo_da_esteira = self.input_modelo_da_esteira.currentText()
        self.novo()

        self.titulo = ''+self.data_input_tipo_de_maquina+' '+self.data_input_modelo_da_esteira
        self.titulo_da_maquina = QLabel('Titulo da Máquina: '+self.titulo)
        self.titulo_da_maquina.setStyleSheet("QLabel { color : black; font-weight: bold; }")
        self.layout_principal.addWidget(self.titulo_da_maquina,1,0,Qt.AlignmentFlag.AlignTop)        

        self.configuracao_de_maquina = QLabel('Configuração de Máquina') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)

        self.configuracao_da_esteira = QLabel('Qual a configurção da esteira?')
        self.layout_principal.addWidget(self.configuracao_da_esteira,2,0,Qt.AlignmentFlag.AlignTop)

        self.input_configuracao_da_esteira = QComboBox(self)
        self.input_configuracao_da_esteira.setFixedHeight(22)
        self.input_configuracao_da_esteira.setPlaceholderText('nenhum')
        self.input_configuracao_da_esteira.addItems(['nenhum',
                                        'horizontal',
                                        'inclinada',
                                        'horizontal para inclinada',
                                        'nose over',
                                        'Z'])
        self.input_configuracao_da_esteira.currentIndexChanged.connect(self.show_titulo_da_maquina)
        self.layout_principal.addWidget(self.input_configuracao_da_esteira,2,1)
        print('configuracao_da_esteira')

    def show_titulo_da_maquina(self):
        self.data_input_configuracao_da_esteira = self.input_configuracao_da_esteira.currentText()
        self.novo()

        self.configuracao_de_maquina = QLabel('Configuração de Máquina') 
        self.configuracao_de_maquina.setStyleSheet("QLabel { color : blue; }")
        self.layout_principal.addWidget(self.configuracao_de_maquina,0,0,Qt.AlignmentFlag.AlignTop)

        self.titulo = ''+self.data_input_tipo_de_maquina+' '+self.data_input_modelo_da_esteira+' '+self.data_input_configuracao_da_esteira

        self.titulo_da_maquina = QLabel('Titulo da Máquina: '+self.titulo)
        self.titulo_da_maquina.setStyleSheet("QLabel { color : black; font-weight: bold; }")
        self.layout_principal.addWidget(self.titulo_da_maquina,1,0,Qt.AlignmentFlag.AlignTop)
        self.show_nome_do_cliente()
        self.show_numero_da_of()
        self.show_data_de_emissao()

    def show_nome_do_cliente(self):
        self.nome_do_cliente = QLabel('Nome do cliente: ')
        self.layout_principal.addWidget(self.nome_do_cliente,2,0,Qt.AlignmentFlag.AlignTop)
        self.input_nome_do_cliente = QLineEdit()
        self.layout_principal.addWidget(self.input_nome_do_cliente,2,1,Qt.AlignmentFlag.AlignTop)

    def show_numero_da_of(self):
        self.numero_da_of = QLabel('Numero da OF: ')
        self.layout_principal.addWidget(self.numero_da_of,3,0,Qt.AlignmentFlag.AlignTop)
        self.input_numero_da_of = QLineEdit()
        self.input_numero_da_of.setPlaceholderText('x.xxx.xxx')
        self.layout_principal.addWidget(self.input_numero_da_of,3,1,Qt.AlignmentFlag.AlignTop) 

    def show_data_de_emissao(self):
        self.input_data_de_emissao = QDateEdit(calendarPopup=True)
      
        self.input_data_de_emissao.setDateTime(QtCore.QDateTime.currentDateTime())
        self.layout_principal.addWidget(self.input_data_de_emissao,4,1,Qt.AlignmentFlag.AlignTop)       

    def show_layout_velocidade_e_carga_no_eixo(self):
        self.novo()
        print('show_layout_velocidade_e_carga_no_eixo')

        self.velocidade_e_carga_no_eixo = QLabel('velocidade_e_carga_no_eixo') 
        self.velocidade_e_carga_no_eixo.setStyleSheet("QLabel { color : blue; }")
        
        self.layout_principal.addWidget(self.velocidade_e_carga_no_eixo,0,0,Qt.AlignmentFlag.AlignTop)
        pass
        

    def novo(self):
        try:          
            for i in reversed(range(self.layout_principal.count())): 
                self.layout_principal.itemAt(i).widget().setParent(None)
        except:
            print('erro widgets no layout_principal nao existem ainda')
           
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
app.setStyleSheet('.QLabel { font-size: 14pt;} .QLineEdit { font-size: 14pt;} .QComboBox { font-size: 14pt;}')
sys.exit(qt.exec())