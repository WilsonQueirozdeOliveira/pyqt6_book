import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tec_system')
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_ComputerIcon')
        icon = self.style().standardIcon(pixmapi)
        
        self.setWindowIcon(icon)
        self.setGeometry(0,0,1000,800)
        self.Interface()

    def Interface(self):

        # layout_principal
        self.main_widget = QWidget()
        #self.main_widget.setStyleSheet('background-color: #999; color: #111;')
        self.scroll = QScrollArea()
        self.scroll.setStyleSheet('background-color: #bbb; color: #111;')
        self.layout_principal = QVBoxLayout()
        paginas = QStackedWidget()
        

        # Barra de menu
        barra_menu = self.menuBar()
        #barra_menu.setStyleSheet('background-color: #bbb; color: #111;')

        menu_calcular = barra_menu.addMenu('Calcular')

        menu_configuracao_de_maquina = menu_calcular.addMenu('Configuração de Máquina')
        botao_maquina_modelo_1 = QAction('Máquina modelo 1', self)
        menu_configuracao_de_maquina.addAction(botao_maquina_modelo_1)
        menu_configuracao_de_maquina.triggered.connect(lambda: paginas.setCurrentIndex(1))
        # add a call to the layout of maquina modelo 1
        botao_maquina_modelo_2 = QAction('Máquina modelo 2', self)
        menu_configuracao_de_maquina.addAction(botao_maquina_modelo_2)
        # add a call to the layout of maquina modelo 2
        #menu_calcular_sub_velocidade_e_carga_de_eixo.triggered.connect(self.show_layout_velocidade_e_carga_no_eixo)

        menu_calcular_sub_velocidade_e_carga_de_eixo = QAction('velocidade e Carga no Eixo', self)
        menu_calcular.addAction(menu_calcular_sub_velocidade_e_carga_de_eixo)
        menu_calcular_sub_velocidade_e_carga_de_eixo.triggered.connect(lambda: paginas.setCurrentIndex(2))
        #menu_calcular_sub_velocidade_e_carga_de_eixo.triggered.connect(self.show_layout_velocidade_e_carga_no_eixo)

        menu_calcular_sub_veliculo_eletrico = QAction('Veículo Elétrico', self)
        menu_calcular.addAction(menu_calcular_sub_veliculo_eletrico)
        menu_calcular_sub_veliculo_eletrico.triggered.connect(self.novo)

        # sobre
        menu_ajuda = barra_menu.addMenu('sobre')
        menu_ajuda_versao = QAction('Versão', self)
        menu_ajuda.addAction(menu_ajuda_versao)
        
        # Barra de ferramentas
        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.setStyleSheet('background-color: #bbb; color: #111;')
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

        #### paginas ####

        # inicio pagina 0
        pagina_inicial = QWidget()
        layout_inicial = QVBoxLayout()
        pagina_inicial.setLayout(layout_inicial)
        titulo_inicial = QLabel('Início')
        layout_inicial.addWidget(titulo_inicial)
        paginas.addWidget(pagina_inicial)

        # pagina 1
        pagina_maquina_modelo_1 = QWidget()
        layout_maquina_modelo_1 = QVBoxLayout()
        pagina_maquina_modelo_1.setLayout(layout_maquina_modelo_1)
        titulo_maquina_modelo_1 = QLabel('maquina modelo 1\n text test\n text test2')
        layout_maquina_modelo_1.addWidget(titulo_maquina_modelo_1)
        paginas.addWidget(pagina_maquina_modelo_1)

        # pagina 2
        pagina_velocidade_e_carga_no_eixo = QWidget()
        layout_velocidade_e_carga_no_eixo = QVBoxLayout()
        pagina_velocidade_e_carga_no_eixo.setLayout(layout_velocidade_e_carga_no_eixo)
        titulo_velocidade_e_carga_no_eixo = QLabel('titulo_velocidade_e_carga_no_eixo')
        #titulo_velocidade_e_carga_no_eixo.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        #titulo_velocidade_e_carga_no_eixo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #titulo_velocidade_e_carga_no_eixo.setFixedWidth(400)
        #titulo_velocidade_e_carga_no_eixo.setFixedHeight(50)
        layout_velocidade_e_carga_no_eixo.addWidget(titulo_velocidade_e_carga_no_eixo)
        #pagina_velocidade_e_carga_no_eixo.setStyleSheet('background-color: #999; color: #111;;')
        paginas.addWidget(pagina_velocidade_e_carga_no_eixo)

        # configurações gerais da gui (executar janela)
        self.main_widget.setLayout(self.layout_principal)

        self.layout_principal.addWidget(paginas)

        self.scroll.setWidget(self.main_widget)

        self.setCentralWidget(self.scroll)

        # Connect the currentChanged signal to a slot that updates the layout
        paginas.currentChanged.connect(self.update_layout_size)

        #self.show()
        

    def novo(self):
        print('Novo projeto criado com sucesso.')

    def gerar_pdf(self):
        print('gerar pdf')

    def update_layout_size(self):
        # This method can be used to update the layout size when the page changes
        #self.centralWidget().updateGeometry()
        print('updateGeometry')
        self.updateGeometry()
        #self.adjustSize()

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

# Set the application style to a dark theme (Fusion)
#app.setStyleSheet('.QLabel { font-size: 14pt;} .QLineEdit { font-size: 14pt;}')
qt.setStyleSheet('.QLabel { font-size: 14pt;} .QLineEdit { font-size: 14pt;}')
#app.setStyle(QStyleFactory.create('Fusion'))
app = JanelaPrincipal()
app.show()
sys.exit(qt.exec())