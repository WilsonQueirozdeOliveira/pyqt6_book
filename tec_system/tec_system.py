from ast import arguments
from re import S
import sys 
import math
from fpdf import FPDF
from datetime import datetime
import time

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Automação de cálculos de Dimensionamento')
        #self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(0,30,1270,690)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()

        self.tabs = QTabWidget()

        # tab_configurar_maquina
        self.tab_configurar_maquina = QWidget()
        self.tabs.addTab(self.tab_configurar_maquina, 'Configurar máquina')
        layout_tab_configurar_maquina = QVBoxLayout()

        self.tab_configura_máquinas = QTabWidget()

        #tab ultraline horizontal
        self.tab_u_h = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_h, 'Ultraline - Horizontal')
        layout_tab_u_h = QHBoxLayout()

        # Imput column 0 tab_u_h
        layout_coluna_0_tab_u_h = QVBoxLayout()

        # Titulo Ultraline Horizontal
        u_h = QLabel('Ultraline Horizontal')
        u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_0_tab_u_h.addWidget(u_h)
        
        # Cliente
        layout_cliente_u_h = QHBoxLayout()
        self.cliente_u_h = QLabel('Cliente:')
        layout_cliente_u_h.addWidget(self.cliente_u_h)
        self.input_cliente_u_h = QLineEdit(self)
        self.input_cliente_u_h.setPlaceholderText('nome')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_cliente_u_h.addWidget(self.input_cliente_u_h)
        layout_cliente_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_cliente_u_h)

        # OF
        layout_OF_u_h = QHBoxLayout()
        self.OF_u_h = QLabel('OF:')
        layout_OF_u_h.addWidget(self.OF_u_h)
        self.input_OF_u_h = QLineEdit(self)
        self.input_OF_u_h.setPlaceholderText('x.xxx.xxx')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_OF_u_h.addWidget(self.input_OF_u_h)
        layout_OF_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_OF_u_h)

        # data_de_emissao
        layout_data_de_emissao_u_h = QHBoxLayout()
        self.data_de_emissao_u_h = QLabel('Data de Emissão:')
        layout_data_de_emissao_u_h.addWidget(self.data_de_emissao_u_h)
        self.input_data_de_emissao_u_h = QLineEdit(self)
        self.input_data_de_emissao_u_h.setPlaceholderText('xx/xx/xxxx')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_data_de_emissao_u_h.addWidget(self.input_data_de_emissao_u_h)
        layout_data_de_emissao_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_data_de_emissao_u_h)

        # data_de_entrega
        layout_data_de_entrega_u_h = QHBoxLayout()
        self.data_de_entrega_u_h = QLabel('Data de Entrega:')
        layout_data_de_entrega_u_h.addWidget(self.data_de_entrega_u_h)
        self.input_data_de_entrega_u_h = QLineEdit(self)
        self.input_data_de_entrega_u_h.setPlaceholderText('xx/xx/xxxx')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_data_de_entrega_u_h.addWidget(self.input_data_de_entrega_u_h)
        layout_data_de_entrega_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_data_de_entrega_u_h)

        # comprimento_util
        layout_comprimento_util_u_h = QHBoxLayout()
        self.comprimento_util_u_h = QLabel('Comprimento Útil[mm]:')
        layout_comprimento_util_u_h.addWidget(self.comprimento_util_u_h)
        self.input_comprimento_util_u_h = QLineEdit(self)
        self.input_comprimento_util_u_h.setPlaceholderText('mm')
        self.input_comprimento_util_u_h.textChanged.connect(self.calcular_u_h)
        layout_comprimento_util_u_h.addWidget(self.input_comprimento_util_u_h)
        layout_comprimento_util_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_comprimento_util_u_h)

        # Comprimento Útil pol
        self.comprimento_util_pol_u_h = QLabel('Comprimento Útil [pol]: ')
        layout_coluna_0_tab_u_h.addWidget(self.comprimento_util_pol_u_h)
        # Comprimento Útil pes
        self.comprimento_util_pes_u_h = QLabel('Comprimento Útil [pes]: ')
        layout_coluna_0_tab_u_h.addWidget(self.comprimento_util_pes_u_h)

        # largura_util
        layout_largura_util_u_h = QHBoxLayout()
        self.largura_util_u_h = QLabel('Largura Útil [mm]:')
        layout_largura_util_u_h.addWidget(self.largura_util_u_h)
        self.input_largura_util_u_h = QLineEdit(self)
        self.input_largura_util_u_h.setPlaceholderText('mm')
        self.input_largura_util_u_h.textChanged.connect(self.calcular_u_h)
        layout_largura_util_u_h.addWidget(self.input_largura_util_u_h)
        layout_largura_util_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_largura_util_u_h)

        # largura Útil pol
        self.largura_util_pol_u_h = QLabel('Largura Útil [pol]: ')
        layout_coluna_0_tab_u_h.addWidget(self.largura_util_pol_u_h)

        # altura_u_h
        layout_altura_u_h = QHBoxLayout()
        self.altura_u_h = QLabel('Altura Útil [mm]:')
        layout_altura_u_h.addWidget(self.altura_u_h)
        self.input_altura_u_h = QLineEdit(self)
        self.input_altura_u_h.setPlaceholderText('mm')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_altura_u_h.addWidget(self.input_altura_u_h)
        layout_altura_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_altura_u_h)

        # pintura
        layout_pintura_u_h = QHBoxLayout()
        self.pintura_u_h = QLabel('Pintura:')
        layout_pintura_u_h.addWidget(self.pintura_u_h)
        self.input_pintura_u_h = QComboBox(self)
        self.input_pintura_u_h.setPlaceholderText('0')
        self.input_pintura_u_h.addItems(['0',
                                                        'Preto (Padrão Ultraline)',
                                                        'Bege RAL 7032 (Padrão Premier)',
                                                        'Especial'])
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_pintura_u_h.addWidget(self.input_pintura_u_h)
        layout_pintura_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_pintura_u_h)

        # modelo_motoredutor
        layout_modelo_motoredutor_u_h = QHBoxLayout()
        self.modelo_motoredutor_u_h = QLabel('Modelo do Motoredutor:')
        layout_modelo_motoredutor_u_h.addWidget(self.modelo_motoredutor_u_h)
        self.input_modelo_motoredutor_u_h = QComboBox(self)
        self.input_modelo_motoredutor_u_h.setPlaceholderText('0')
        self.input_modelo_motoredutor_u_h.addItems(['0',
                                                                    'GSA 28','GSA 41 (Padrão)',
                                                                    'GSA 51','GSA 63','GS 75'])
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_modelo_motoredutor_u_h.addWidget(self.input_modelo_motoredutor_u_h)
        layout_modelo_motoredutor_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_modelo_motoredutor_u_h)

        # posicao_motoredutor
        layout_posicao_motoredutor_u_h = QHBoxLayout()
        self.posicao_motoredutor_u_h = QLabel('Posição do Motoredutor:')
        layout_posicao_motoredutor_u_h.addWidget(self.posicao_motoredutor_u_h)
        self.input_posicao_motoredutor_u_h = QComboBox(self)
        self.input_posicao_motoredutor_u_h.setPlaceholderText('0')
        self.input_posicao_motoredutor_u_h.addItems(['0',
                                                                    'Esquerdo (puxando)','Esquerdo (empurrando)',
                                                                    'Direito (puxando)','Direito (empurrando)'])
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_posicao_motoredutor_u_h.addWidget(self.input_posicao_motoredutor_u_h)
        layout_posicao_motoredutor_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_posicao_motoredutor_u_h)

        # modelo_cuba
        layout_modelo_cuba_u_h = QHBoxLayout()
        self.modelo_cuba_u_h = QLabel('Modelo da Cuba:')
        layout_modelo_cuba_u_h.addWidget(self.modelo_cuba_u_h)
        self.input_modelo_cuba_u_h = QComboBox(self)
        self.input_modelo_cuba_u_h.setPlaceholderText('0')
        self.input_modelo_cuba_u_h.addItems(['0','Sem cuba','Padrão',
                                                            'Padrão sem lado Direito',
                                                            'Padrão sem lado Esquerdo','Especial'])
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_modelo_cuba_u_h.addWidget(self.input_modelo_cuba_u_h)
        layout_modelo_cuba_u_h.addStretch()
        
        layout_coluna_0_tab_u_h.addLayout(layout_modelo_cuba_u_h)

        # fim vbox layout_coluna_0_tab_u_h
        layout_coluna_0_tab_u_h.addStretch()

        # Imput column 1 tab_u_h
        layout_coluna_1_tab_u_h = QVBoxLayout()

        # Titulo Montagem
        Montagem_u_h = QLabel('Montagem')
        Montagem_u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_1_tab_u_h.addWidget(Montagem_u_h)

        # perfil_lateral
        self.perfil_lateral_u_h = QLabel('Perfil Lateral [mm]: ')
        layout_coluna_1_tab_u_h.addWidget(self.perfil_lateral_u_h)

        # perfil_travessa
        self.perfil_travessa_u_h = QLabel('Perfil Travessa [mm]: ')
        layout_coluna_1_tab_u_h.addWidget(self.perfil_travessa_u_h)

        # chapa de apoio
        self.chapa_apoio_u_h = QLabel('Chapa de apoio:L[mm]xC[mm] ')
        layout_coluna_1_tab_u_h.addWidget(self.chapa_apoio_u_h)

        # guias laterais
        self.guias_u_h = QLabel('Guias/Corte[mm]: ')
        layout_coluna_1_tab_u_h.addWidget(self.guias_u_h)

        # Fixador em ângulo
        fixador_em_angulo_u_h = QLabel('Fixador em ângulo: U.004.001')
        layout_coluna_1_tab_u_h.addWidget(fixador_em_angulo_u_h)

        # Mancal para Rolo de tração
        mancal_tracao_u_h = QLabel('Mancal de tração: Escolha Motoredutor')
        layout_coluna_1_tab_u_h.addWidget(mancal_tracao_u_h)

        # Mancal para Rolo libre
        mancal_livre_u_h = QLabel('Mancal livre: T.515.002.00.00')
        layout_coluna_1_tab_u_h.addWidget(mancal_livre_u_h)

        # pernas
        pernas_u_h = QLabel('Pernas ')
        layout_coluna_1_tab_u_h.addWidget(pernas_u_h)

        # perfil U
        self.perfil_U_u_h = QLabel('Perfil U [mm]: ')
        layout_coluna_1_tab_u_h.addWidget(self.perfil_U_u_h)

        # perna tubo quadrado
        perna_tubo_quadrado_u_h = QLabel('Perna tubo quadrado [mm]: ')
        layout_coluna_1_tab_u_h.addWidget(perna_tubo_quadrado_u_h)

        # Rodízio c/ Freio =
        rodizio_F_u_h = QLabel('Rodízio c/ Freio [mm]: GLE 312 NTE G')
        layout_coluna_1_tab_u_h.addWidget(rodizio_F_u_h)
        
        # Tubo Quad. entre pernas =
        tubo_interno_u_h = QLabel('Tubo Quad. entre pernas [mm]: ')
        layout_coluna_1_tab_u_h.addWidget(tubo_interno_u_h)

        # correia
        correia_u_h = QLabel('Correia')
        correia_u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_1_tab_u_h.addWidget(correia_u_h)

        # largura da correia
        largura_correia_u_h = QLabel('Largura da correira:')
        layout_coluna_1_tab_u_h.addWidget(largura_correia_u_h)

        # Comprimento da correia
        comprimento_correia_u_h = QLabel('Comprimento da correira:')
        layout_coluna_1_tab_u_h.addWidget(comprimento_correia_u_h)

        # Cor da correia
        cor_correia_u_h = QLabel('Cor da correira:')
        layout_coluna_1_tab_u_h.addWidget(cor_correia_u_h)

        # passo da talisca
        passo_talisca_u_h = QLabel('Passo da talisca:')
        layout_coluna_1_tab_u_h.addWidget(passo_talisca_u_h)

        # altura da talisca
        altura_talisca_u_h = QLabel('Altura da talisca:')
        layout_coluna_1_tab_u_h.addWidget(altura_talisca_u_h)

        # borda_sanfonada
        borda_sanfonada_u_h = QLabel('Borda Sanfonada:')
        layout_coluna_1_tab_u_h.addWidget(borda_sanfonada_u_h)

        # fim vbox layout_coluna_1_tab_u_h
        layout_coluna_1_tab_u_h.addStretch()

        layout_coluna_2_tab_u_h = QVBoxLayout()

        # usinagem
        usinagem_u_h = QLabel('Usinagem')
        usinagem_u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_2_tab_u_h.addWidget(usinagem_u_h)

        # material do tubo_tracao
        material_tubo_tracao_u_h = QLabel('Material do tubo de tração: ')
        layout_coluna_2_tab_u_h.addWidget(material_tubo_tracao_u_h)

        # comprimento do tubo_tracao
        comprimento_tubo_tracao_u_h = QLabel('Comprimento do Tubo de Tração: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_tubo_tracao_u_h)

        # material do eixo_tracao
        material_eixo_tracao_u_h = QLabel('Material do Eixo de Tração: ')
        layout_coluna_2_tab_u_h.addWidget(material_eixo_tracao_u_h)

        # comprimento do eixo_tracao
        comprimento_eixo_tracao_u_h = QLabel('Comprimento do Eixo de tração: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_eixo_tracao_u_h)

        # material do tubo_livre
        material_tubo_livre_u_h = QLabel('Material do Tubo Livre: ')
        layout_coluna_2_tab_u_h.addWidget(material_tubo_livre_u_h)

        # comprimento do tubo_livre
        comprimento_tubo_livre_u_h = QLabel('Comprimento do Tubo Livre: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_tubo_livre_u_h)

        # material do eixo_livre
        material_eixo_livre_u_h = QLabel('Material do Eixo Livre: ')
        layout_coluna_2_tab_u_h.addWidget(material_eixo_livre_u_h)

        # comprimento do eixo_livre
        comprimento_eixo_livre_u_h = QLabel('Comprimento do Eixo Livre: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_eixo_livre_u_h)

        # material do tubo_inferior
        material_tubo_inferior_u_h = QLabel('Material do Tubo Inferior: ')
        layout_coluna_2_tab_u_h.addWidget(material_tubo_inferior_u_h)

        # comprimento do tubo_inferior
        comprimento_tubo_inferior_u_h = QLabel('Comprimento do Tubo Inferior: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_tubo_inferior_u_h)

        # material do eixo_inferior
        material_eixo_inferior_u_h = QLabel('Material do Eixo Inferior: ')
        layout_coluna_2_tab_u_h.addWidget(material_eixo_inferior_u_h)

        # comprimento do eixo_inferior
        comprimento_eixo_inferior_u_h = QLabel('Comprimento do Eixo Inferior: ')
        layout_coluna_2_tab_u_h.addWidget(comprimento_eixo_inferior_u_h)

        # Eletrica
        eletrica_u_h = QLabel('Elétrica')
        eletrica_u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_2_tab_u_h.addWidget(eletrica_u_h)

        # acionamento eletrico
        layout_acionamento_u_h = QHBoxLayout()
        self.acionamento_u_h = QLabel('Acionamento Elético: ')
        layout_acionamento_u_h.addWidget(self.acionamento_u_h)
        self.input_acionamento_u_h = QComboBox(self)
        self.input_acionamento_u_h.setPlaceholderText('0')
        self.input_acionamento_u_h.addItems(['0',
                                            'Chave Liga / Desliga',
                                            'Painel Liga / Desliga',
                                            'Painel Liga / Desliga c/ Inversor',
                                            'Painel Passo Indexado',
                                            'Painel Passo Indexado c/ Inversor',
                                            'Painel Especial (Ver Notas Gerais)'])                                                    	
	
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_acionamento_u_h.addWidget(self.input_acionamento_u_h)
        layout_acionamento_u_h.addStretch()
        
        layout_coluna_2_tab_u_h.addLayout(layout_acionamento_u_h)

        # alimentacao
        layout_alimentacao_u_h = QHBoxLayout()
        self.alimentacao_u_h = QLabel('Alimentação: ')
        layout_alimentacao_u_h.addWidget(self.alimentacao_u_h)
        self.input_alimentacao_u_h = QComboBox(self)
        self.input_alimentacao_u_h.setPlaceholderText('0')
        self.input_alimentacao_u_h.addItems(['0',
                                            'Plug 3P + T 16A / 220V',
                                            'Plug 3P + T 16A / 380V',
                                            'Plug 3P + T 16A / 440V',
                                            'Plug 3P + T 32A / 220V',
                                            'Plug 3P + T 32A / 380V',
                                            'Plug 3P + T 32A / 440V',
                                            'Plug 3P + N + T 16A / 220V(5pinos)',
                                            'Plug 3P + N + T 16A / 380V(5pinos)',
                                            'Plug 3P + N + T 16A / 440V(5pinos)',
                                            'Plug 3P + N + T 32A / 220V(5pinos)',
                                            'Plug 3P + N + T 32A / 380V(5pinos)',
                                            'Plug 3P + N + T 32A / 440V(5pinos)',
                                            '220V',
                                            '380V',
                                            '440V',])                                          	
	
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_alimentacao_u_h.addWidget(self.input_alimentacao_u_h)
        layout_alimentacao_u_h.addStretch()
        
        layout_coluna_2_tab_u_h.addLayout(layout_alimentacao_u_h)

        # comprimento_cabo
        layout_comprimento_cabo_u_h = QHBoxLayout()
        self.comprimento_cabo_u_h = QLabel('Comprimento do cabo [m]:')
        layout_comprimento_cabo_u_h.addWidget(self.comprimento_cabo_u_h)
        self.input_comprimento_cabo_u_h = QLineEdit(self)
        self.input_comprimento_cabo_u_h.setPlaceholderText('mm')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_comprimento_cabo_u_h.addWidget(self.input_comprimento_cabo_u_h)
        layout_comprimento_cabo_u_h.addStretch()
        
        layout_coluna_2_tab_u_h.addLayout(layout_comprimento_cabo_u_h)

        # comando
        layout_comando_u_h = QHBoxLayout()
        self.comando_u_h = QLabel('Comando: ')
        layout_comando_u_h.addWidget(self.comando_u_h)
        self.input_comando_u_h = QComboBox(self)
        self.input_comando_u_h.setPlaceholderText('0')
        self.input_comando_u_h.addItems(['0',
                                            '24 V',
                                            '220 V',
                                            '380 V',
                                            '440 V'])   

        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_comando_u_h.addWidget(self.input_comando_u_h)
        layout_comando_u_h.addStretch()
        
        layout_coluna_2_tab_u_h.addLayout(layout_comando_u_h)

        # seguranca
        layout_seguranca_u_h = QHBoxLayout()
        self.seguranca_u_h = QLabel('Segurança: ')
        layout_seguranca_u_h.addWidget(self.seguranca_u_h)
        self.input_seguranca_u_h = QComboBox(self)
        self.input_seguranca_u_h.setPlaceholderText('0')
        self.input_seguranca_u_h.addItems(['0',
                                            'Padrão',
                                            'NR-12'])   

        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_seguranca_u_h.addWidget(self.input_seguranca_u_h)
        layout_seguranca_u_h.addStretch()
        
        layout_coluna_2_tab_u_h.addLayout(layout_seguranca_u_h)

               


        # fim vbox layout_coluna_2_tab_u_h
        layout_coluna_2_tab_u_h.addStretch()

        layout_coluna_3_tab_u_h = QVBoxLayout()

        # Notas Gerais
        layout_notas_gerais = QVBoxLayout()
        notas_gerais_u_h = QLabel('Notas Gerais: ')
        layout_notas_gerais.addWidget(notas_gerais_u_h)
        self.input_notas_gerais = QTextEdit(self)
        layout_notas_gerais.addWidget(self.input_notas_gerais)
        layout_coluna_3_tab_u_h.addLayout(layout_notas_gerais) 

        # custos
        custos_u_h = QLabel('Custos')
        custos_u_h.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_3_tab_u_h.addWidget(custos_u_h)

        # fim vbox layout_coluna_3_tab_u_h
        layout_coluna_3_tab_u_h.addStretch()
       
        # fim hbox layout_tab_u_h
        layout_tab_u_h.addLayout(layout_coluna_0_tab_u_h)
        layout_tab_u_h.addLayout(layout_coluna_1_tab_u_h)
        layout_tab_u_h.addLayout(layout_coluna_2_tab_u_h)
        layout_tab_u_h.addLayout(layout_coluna_3_tab_u_h)
        layout_tab_u_h.addStretch()

        # fim vbox tab_u_h
        self.tab_u_h.setLayout(layout_tab_u_h)
        
    ####################################

        #tab ultraline inclinada
        self.tab_u_i = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_i, 'Ultraline - Inclinada')
        layout_tab_u_i = QHBoxLayout()

        layout_coluna_0_tab_u_i =QVBoxLayout()

        # altura_de_entrada
        layout_altura_de_entrada_u_i = QHBoxLayout()
        self.altura_de_entrada_u_i = QLabel('Altura de Entrada [mm]:')
        layout_altura_de_entrada_u_i.addWidget(self.altura_de_entrada_u_i)
        self.input_altura_de_entrada_u_i = QLineEdit(self)
        self.input_altura_de_entrada_u_i.setPlaceholderText('mm')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_altura_de_entrada_u_i.addWidget(self.input_altura_de_entrada_u_i)
        layout_altura_de_entrada_u_i.addStretch()
        
        layout_coluna_0_tab_u_i.addLayout(layout_altura_de_entrada_u_i)

        # altura_de_saida
        layout_altura_de_saida_u_i = QHBoxLayout()
        self.altura_de_saida_u_i = QLabel('Altura de Saída [mm]:')
        layout_altura_de_saida_u_i.addWidget(self.altura_de_saida_u_i)
        self.input_altura_de_saida_u_i = QLineEdit(self)
        self.input_altura_de_saida_u_i.setPlaceholderText('mm')
        #self.input_cliente.textChanged.connect(self.calcular_ultraline)
        layout_altura_de_saida_u_i.addWidget(self.input_altura_de_saida_u_i)
        layout_altura_de_saida_u_i.addStretch()
        
        layout_coluna_0_tab_u_i.addLayout(layout_altura_de_saida_u_i)

        layout_tab_u_i.addLayout(layout_coluna_0_tab_u_i)
        #

        self.tab_u_i.setLayout(layout_tab_u_i)

        #tab ultraline horizontal para inclinada
        self.tab_u_h_para_inclinada = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_h_para_inclinada, 'Ultraline - horizontal para Inclinada')
        layout_tab_u_h_para_inclinada = QVBoxLayout()

        self.tab_u_h_para_inclinada.setLayout(layout_tab_u_h_para_inclinada)

        #tab ultraline nose over
        self.tab_ultraline_nose_over = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_ultraline_nose_over, 'Ultraline - Nose Over')
        layout_tab_ultraline_nose_over = QVBoxLayout()

        self.tab_ultraline_nose_over.setLayout(layout_tab_ultraline_nose_over)

        #tab ultraline Z
        self.tab_ultraline_z = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_ultraline_z, 'Ultraline - "Z"')
        layout_tab_ultraline_z = QVBoxLayout()

        self.tab_ultraline_z.setLayout(layout_tab_ultraline_z)

        #tab Premiere Horizontal
        self.tab_premiere_horizontal = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_premiere_horizontal, 'Premiere - Horizontal')
        layout_tab_premiere_horizontal = QVBoxLayout()

        self.tab_premiere_horizontal.setLayout(layout_tab_premiere_horizontal)

        #tab Premiere inclinada
        self.tab_premiere_inclinada = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_premiere_inclinada, 'Premiere - Inclinada')
        layout_tab_premiere_inclinada = QVBoxLayout()

        self.tab_premiere_inclinada.setLayout(layout_tab_premiere_inclinada)

        #tab Premiere horizontal para inclinada
        self.tab_premiere_horizontal_para_inclinada = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_premiere_horizontal_para_inclinada, 'Premiere - Horizontal para Inclinada')
        layout_tab_premiere_horizontal_para_inclinada = QVBoxLayout()

        self.tab_premiere_horizontal_para_inclinada.setLayout(layout_tab_premiere_horizontal_para_inclinada)

        #tab classic Horizontal
        self.tab_classic_horizontal = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_classic_horizontal, 'Classic - Horizontal')
        layout_tab_classic_horizontal = QVBoxLayout()

        self.tab_classic_horizontal.setLayout(layout_tab_classic_horizontal)

        #tab classic inclinada
        self.tab_classic_inclinada = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_classic_inclinada, 'Classic - Inclinada')
        layout_tab_classic_inclinada = QVBoxLayout()

        self.tab_classic_inclinada.setLayout(layout_tab_classic_inclinada)

        #tab Super classic Horizontal
        self.tab_super_classic_horizontal = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_super_classic_horizontal, 'Super Classic - Horizontal')
        layout_tab_super_classic_horizontal = QVBoxLayout()

        self.tab_super_classic_horizontal.setLayout(layout_tab_super_classic_horizontal)

        #tab super classic inclinada
        self.tab_super_classic_inclinada = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_super_classic_inclinada, 'Super Classic - Inclinada')
        layout_tab_super_classic_inclinada = QVBoxLayout()

        self.tab_super_classic_inclinada.setLayout(layout_tab_super_classic_inclinada)

        #tab ultraline horizontal modular
        self.tab_u_h_modular = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_h_modular, 'Ultraline - Horizontal Modular')
        layout_tab_u_h_modular = QVBoxLayout()

        self.tab_u_h_modular.setLayout(layout_tab_u_h_modular)

        #tab ultraline inclinada modular
        self.tab_u_i_modular = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_i_modular, 'Ultraline - Inclinada Modular')
        layout_tab_u_i_modular = QVBoxLayout()

        self.tab_u_i_modular.setLayout(layout_tab_u_i_modular)

        #tab ultraline horizontal para inclinada modular
        self.tab_u_h_para_inclinada_modular = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_u_h_para_inclinada_modular , 'Ultraline - Horizontal para Inclinada Modulor')
        layout_tab_u_h_para_inclinada_modular  = QVBoxLayout()

        self.tab_u_h_para_inclinada_modular.setLayout(layout_tab_u_h_para_inclinada_modular)

        #tab drum
        self.tab_drum = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_drum , 'Drum')
        layout_tab_drum  = QVBoxLayout()

        self.tab_drum.setLayout(layout_tab_drum)

        #tab box
        self.tab_box = QWidget()
        self.tab_configura_máquinas.addTab(self.tab_box , 'Box')
        layout_tab_box  = QVBoxLayout()

        self.tab_box.setLayout(layout_tab_box)


        # Fim layout tab configurar máquinas
        layout_tab_configurar_maquina.addWidget(self.tab_configura_máquinas)

        # tab_calculos_de_transporte
        self.tab_calculos_de_transporte = QWidget()
        self.tabs.addTab(self.tab_calculos_de_transporte, 'Cálculos de transporte')
        layout_tab_calculos_de_transporte = QHBoxLayout()

        # Imput column 0 tab_calculos_de_transporte
        layout_coluna_0_tab_calculos_de_transporte = QVBoxLayout()

        # Title
        velocidade_do_motor = QLabel('Velocidade do Motor')
        velocidade_do_motor.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_0_tab_calculos_de_transporte.addWidget(velocidade_do_motor)
        
        #frequency
        layout_frequencia = QHBoxLayout()
        self.frequencia = QLabel('Frequência [Hz]:')
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.frequencia)
        layout_frequencia.addWidget(self.frequencia)
        self.input_frequencia = QLineEdit(self)
        self.input_frequencia.setPlaceholderText('Hz')
        self.input_frequencia.textChanged.connect(self.calcular_transporte)
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.input_frequencia)
        layout_frequencia.addWidget(self.input_frequencia)
        layout_frequencia.addStretch()
        layout_coluna_0_tab_calculos_de_transporte.addLayout(layout_frequencia)
        
        # Poles
        layout_polos = QHBoxLayout()
        self.polos = QLabel('Polos [Nº]:')
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.polos)
        layout_polos.addWidget(self.polos)
        self.input_polos = QLineEdit(self)
        self.input_polos.setPlaceholderText('Nº(2-4-6-8-16)')
        self.input_polos.textChanged.connect(self.calcular_transporte)
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.input_polos)
        layout_polos.addWidget(self.input_polos)
        layout_polos.addStretch()
        layout_coluna_0_tab_calculos_de_transporte.addLayout(layout_polos)

        # Pear fo poles
        self.par_de_polos = QLabel('Par de Polos [Nº]: ')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.par_de_polos)
        
        self.rps = QLabel('RPS:')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.rps)

        # RPM
        self.rpm = QLabel('RPM:')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.rpm)

        #slip
        layout_escorregamento = QHBoxLayout()
        self.escorregamento = QLabel('Escorregamento [%]:')
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.escorregamento)
        layout_escorregamento.addWidget(self.escorregamento)
        self.input_escorregamento = QLineEdit(self)
        self.input_escorregamento.setPlaceholderText('0.0%')
        self.input_escorregamento.textChanged.connect(self.calcular_transporte)
        #layout_coluna_0_tab_calculos_de_transporte.addWidget(self.input_escorregamento)
        layout_escorregamento.addWidget(self.input_escorregamento)
        layout_escorregamento.addStretch()
        layout_coluna_0_tab_calculos_de_transporte.addLayout(layout_escorregamento)

        # RPM ~Real
        self.rpm_real = QLabel('RPM de Saida ~Real: ')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.rpm_real)

        # Reduction velocity
        velocidade_da_reducao = QLabel('Velociadade da redução')
        velocidade_da_reducao.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_0_tab_calculos_de_transporte.addWidget(velocidade_da_reducao)

        # Reduction
        layout_reducao = QHBoxLayout()
        self.reducao = QLabel('Redução [1/X]: ')
        layout_reducao.addWidget(self.reducao)
        self.input_reducao = QLineEdit(self)
        self.input_reducao.setPlaceholderText('X')
        layout_reducao.addWidget(self.input_reducao)
        self.input_reducao.textChanged.connect(self.calcular_transporte)
        layout_reducao.addStretch()
        layout_coluna_0_tab_calculos_de_transporte.addLayout(layout_reducao)

        # RPM after Reduction
        self.rpm_apos_reducao = QLabel('RPM após Redução: ')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.rpm_apos_reducao)

        # Cylinder velocity
        velocidade_do_cilindro = QLabel('Velociadade do Cilindro')
        #velocidade_do_cilindro.setStyleSheet("QLabel { background-color : red; color : blue; }")
        velocidade_do_cilindro.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_0_tab_calculos_de_transporte.addWidget(velocidade_do_cilindro)

        # traction diameter 
        layout_diametro_de_tracao = QHBoxLayout()
        self.diametro_do_cilindro = QLabel('Diâmetro do Cilindro de Tração [mm]:')
        layout_diametro_de_tracao.addWidget(self.diametro_do_cilindro)
        self.input_diametro_de_tracao = QLineEdit(self)
        self.input_diametro_de_tracao.setPlaceholderText('0.0 mm')
        layout_diametro_de_tracao.addWidget(self.input_diametro_de_tracao)
        self.input_diametro_de_tracao.textChanged.connect(self.calcular_transporte)
        layout_diametro_de_tracao.addStretch()
        layout_coluna_0_tab_calculos_de_transporte.addLayout(layout_diametro_de_tracao)

        # Cylinder Perimeter
        self.perimetro_do_cilindro = QLabel(
            'Perímetro do Cilindro de Tração [mm]: ')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.perimetro_do_cilindro)

        # Cylinder tangent Velocity
        self.velocidade_tangente = QLabel(
            'Velocidade Tangente [m/min]: ')
        layout_coluna_0_tab_calculos_de_transporte.addWidget(self.velocidade_tangente)

        # end column 0

        layout_coluna_0_tab_calculos_de_transporte.addStretch()

        layout_tab_calculos_de_transporte.addLayout(layout_coluna_0_tab_calculos_de_transporte)

        # Imput column 1 tab_calculos_de_transporte
        layout_coluna_1_tab_calculos_de_transporte = QVBoxLayout()
        
        # Engine Torque
        torque_do_motor = QLabel('Torque do Motor')
        torque_do_motor.setStyleSheet("QLabel { color : blue; }")
        layout_coluna_1_tab_calculos_de_transporte.addWidget(torque_do_motor)

        # Motor voltage
        layout_tensao_do_motor = QHBoxLayout()
        tensao_do_motor = QLabel('Tensão do motor [V]:')
        layout_tensao_do_motor.addWidget(tensao_do_motor)
        self.input_tensao_do_motor = QLineEdit(self)
        self.input_tensao_do_motor.setPlaceholderText('0.0 Volts')
        layout_tensao_do_motor.addWidget(self.input_tensao_do_motor)
        self.input_tensao_do_motor.textChanged.connect(self.calcular_transporte)
        layout_tensao_do_motor.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_tensao_do_motor)

        # Potence factor (fator de potência = FP = COS@*n)
        layout_FP = QHBoxLayout()
        FP = QLabel('Fator de potência [FP]:')
        layout_FP.addWidget(FP)
        self.input_FP = QLineEdit(self)
        self.input_FP.setPlaceholderText('0.0 FP')
        layout_FP.addWidget(self.input_FP)
        self.input_FP.textChanged.connect(self.calcular_transporte)
        layout_FP.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_FP)

        # n = rendimento
        layout_redimento = QHBoxLayout()
        rendimento = QLabel('Rendimento [n]:')
        layout_redimento.addWidget(rendimento)
        self.input_rendimento = QLineEdit(self)
        self.input_rendimento.setPlaceholderText('0.0 n')
        layout_redimento.addWidget(self.input_rendimento)
        self.input_rendimento.textChanged.connect(self.calcular_transporte)
        layout_redimento.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_redimento)

       

        # Corrente nominal 
        layout_corrente = QHBoxLayout()
        corrente = QLabel('Corrente [A]:')
        layout_corrente.addWidget(corrente)
        self.input_corrente = QLineEdit(self)
        self.input_corrente.setPlaceholderText('0.0 A')
        layout_corrente.addWidget(self.input_corrente)
        self.input_corrente.textChanged.connect(self.calcular_transporte)
        layout_corrente.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_corrente)

        # FS = fartor de serviço
        layout_FS = QHBoxLayout()
        FS = QLabel('Fator de serviço [FS]:')
        layout_FS.addWidget(FS)
        self.input_FS = QLineEdit(self)
        self.input_FS.setPlaceholderText('0.0 FS')
        layout_FS.addWidget(self.input_FS)
        self.input_FS.textChanged.connect(self.calcular_transporte)
        layout_FS.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_FS)

        # Potência cv
        self.potencia_cv = QLabel('Potência [CV]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.potencia_cv)

        # Pontência w
        self.potencia_w = QLabel('Potência [W]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.potencia_w)

        # gravidade 9.80665 m/s**2

        # conjugado nominal [kgfm]
        self.conjugado_kgmf = QLabel('Conjugado [kgmf]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.conjugado_kgmf)

        # conjugado nominal [Nm]
        self.conjugado_nm = QLabel('Conjugado [Nm]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.conjugado_nm)

        # Rendimento do redutor [%]
        layout_rendimento_redutor = QHBoxLayout()
        FS = QLabel('Rendimento do redutor [%]:')
        layout_rendimento_redutor.addWidget(FS)
        self.input_rendimento_redutor = QLineEdit(self)
        self.input_rendimento_redutor.setPlaceholderText('0.0 [%]')
        layout_rendimento_redutor.addWidget(self.input_rendimento_redutor)
        self.input_rendimento_redutor.textChanged.connect(self.calcular_transporte)
        layout_rendimento_redutor.addStretch()
        layout_coluna_1_tab_calculos_de_transporte.addLayout(layout_rendimento_redutor)

        # Torque após redutor [Nm]
        self.torque_redutor = QLabel('Torque após redutor [Nm]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.torque_redutor)

        # Força tangente ao cilindro [N]
        self.forca_tagente = QLabel('Força tangente ao cilindro [N]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.forca_tagente)

        # Carga máxima tangente cilindro [kg]
        self.carga_tagente = QLabel('Carga máxima tangente cilindro [kg]: ')
        layout_coluna_1_tab_calculos_de_transporte.addWidget(self.carga_tagente)

        # and column 1

        layout_coluna_1_tab_calculos_de_transporte.addStretch()

        layout_tab_calculos_de_transporte.addLayout(layout_coluna_1_tab_calculos_de_transporte)
        layout_tab_calculos_de_transporte.addStretch()
        
        # tab_calculos_de_produtividade
        self.tab_calculos_de_produtividade = QWidget()
        self.tabs.addTab(self.tab_calculos_de_produtividade, 'Calculos de produtividade')
        layout_tab_calculos_de_produtividade = QHBoxLayout()

        # tab_sobre
        self.tab_sobre = QWidget()
        self.tabs.addTab(self.tab_sobre, 'sobre')
        layout_tab_sobre = QHBoxLayout()

        layout.addWidget(self.tabs)

        self.tab_configurar_maquina.setLayout(layout_tab_configurar_maquina)
        self.tab_calculos_de_transporte.setLayout(layout_tab_calculos_de_transporte)
        self.tab_calculos_de_produtividade.setLayout(layout_tab_calculos_de_produtividade)
        self.tab_sobre.setLayout(layout_tab_sobre)

        #botoes inferiores
        gerar_pdf = QPushButton('Gerar PDF', self)
        gerar_pdf.clicked.connect(self.funcao_gerar_pdf)

        botao_sair = QPushButton('SAIR', self)
        botao_sair.clicked.connect(self.confirma_saida)

        layout_botoes_inferiores = QHBoxLayout()
        
        

        layout_botoes_inferiores.addStretch()
        layout_botoes_inferiores.addWidget(gerar_pdf)
        layout_botoes_inferiores.addWidget(botao_sair)
        #fim botoes inferiores

        layout.addLayout(layout_botoes_inferiores)

        self.setLayout(layout)

        self.show()

    def novo(self):
        print('Novo projeto criado com sucesso.')

    def calcular_u_h(self):

        mm_pol = 25.4
        mm_pes = 304.8

        # Converter comprimanto util
        if self.input_comprimento_util_u_h.text():
            try:
                if isinstance(float(self.input_comprimento_util_u_h.text()),float):
                    comprimento_util_u_h = float(self.input_comprimento_util_u_h.text())
                    comprimento_util_u_h_pol = comprimento_util_u_h/mm_pol
                    comprimento_util_u_h_pes = comprimento_util_u_h/mm_pes
                    self.comprimento_util_pol_u_h.setText('Comprimento Útil [pol]: '+str(comprimento_util_u_h_pol))
                    self.comprimento_util_pes_u_h.setText('Comprimento Útil [pes]: '+str(comprimento_util_u_h_pes))
                    print('converter comprimento_util_u_h_pol')
                    print('converter comprimento_util_u_h_pes')

                    #perfil lateral corte montagem 
                    print('converter comprimento perfil lateral')  
                    perfil_lateral_u_h = comprimento_util_u_h-152.4 # util menos mancal e esticador
                    self.perfil_lateral_u_h.setText('Perfil Lateral [mm]: '+str(perfil_lateral_u_h)) 

                    # guias / corte
                    print('guias  / corte')  
                    guia_u_h = perfil_lateral_u_h + 254.0 # guias
                    corte_guia_u_h = guia_u_h + 205.0 # corte
                    self.guias_u_h.setText('Guias/Corte [mm]:'+str(guia_u_h)+' / '+str(corte_guia_u_h)) 

            except:
                print('erro ao converter comprimento_util_u_h_pol')
                print('erro ao converter comprimento_util_u_h_pes')
                print('erro ao converter comprimento perfil lateral')

        # Converter largura util
        if self.input_largura_util_u_h.text():
            try:
                if isinstance(float(self.input_largura_util_u_h.text()),float):
                    largura_util_u_h = float(self.input_largura_util_u_h.text())
                    largura_util_u_h_pol = largura_util_u_h/mm_pol
                    self.largura_util_pol_u_h.setText('largura Útil [pol]: '+str(largura_util_u_h_pol))

                    print('converter largura_util_u_h_pol')   

                    #perfil travessa corte montagem 
                    print('converter travessa corte montagem')  
                    perfil_travessa_u_h = largura_util_u_h+50.8 # util mais espaço abaixo das guias
                    self.perfil_travessa_u_h.setText('Perfil Travessa [mm]: '+str(perfil_travessa_u_h))   

                    #'Chapa de apoio:L[mm]xC[mm] '     
                    print('converter Chapa de apoio:L[mm]xC[mm]')  
                    L_chapa_de_apoio = largura_util_u_h/2.0 # util dividida espaço de 50.8
                    try:
                        C_chapa_de_apoio = comprimento_util_u_h-mm_pes # util menos um pé
                    except:
                        print('comprimento_util_u_h vazio')
                    self.chapa_apoio_u_h.setText('Chapa de apoio[mm]: L '+str(L_chapa_de_apoio)+'xC '+str(C_chapa_de_apoio))     
            except:
                print('erro ao converter largura_util_u_h_pol')


        '''
        GRA F 204 (com rebaixo no eixo)
        GRA F 204
        GRA F 205
        GRA F 206
        GRA F 207

        '''        

        # fim calcula ultraline horizontal               
        pass

    def calcular_transporte(self):
        #print(self.input_frequencia.text())
        #print(self.input_polos.text())
        #print(self.rps.text())

        input_polos = 0
        par_de_polos = 0
        rpm = 0
        escorregamento =0
        rpm_real = 0
        rpm_apos_reducao = 0
        perimetro_do_cilindro = 0
        tensao_do_motor = 0
        FP = 0
        rendimento = 0
        corrente = 0
        FS = 0
        potencia_w = 0
        conjugado_kgmf = 0
        conjugado_nm = 0
        torque_redutor = 0
        reducao = 0
        rendimento_redutor = 0
        forca_tangente = 0
        carga_tangente = 0
        diametro_de_tracao = 0
        gravidade = 9.80665
        carga_tangente = 0

        
        # Calculate pair of poles
        if self.input_polos.text():
            try:    
                if isinstance(float(self.input_polos.text()),float):
                    input_polos = int(self.input_polos.text())
                    par_de_polos = input_polos/2
                    if input_polos == 2 or input_polos == 4 or input_polos == 8 or input_polos == 16:
                        self.par_de_polos.setText(
                            'Par de Polos [Nº]: '+str(par_de_polos))
                        print('calcula par de polos')
                        self.polos.setText('Polos [Nº]:')
            except:
                print('erro ao converter input polos para float')
                self.polos.setText('Polos [Nº]: Erro. Erro entrada float : 0.0')

        # Calculate RPM
        if self.input_frequencia.text():
            try:
                if isinstance(float(self.input_frequencia.text()),float) and par_de_polos:
                    frequencia = float(self.input_frequencia.text())
                    self.rps.setText('RPS: '+str(frequencia/par_de_polos))
                    rpm = (frequencia/par_de_polos)*60
                    self.rpm.setText('RPM: '+str(rpm)+' Sem escorregamento.')
                    print('calcula rpm')
                    self.frequencia.setText('Frequência [Hz]:')
            except:
                print('erro ao converter input_frequencia para float')
                self.frequencia.setText('Frequência[Hz]: Erro. entrada float : 0.0')

        # Calculate ~Real RPM
        if self.input_escorregamento.text():
            try:
                if isinstance(float(self.input_escorregamento.text()),float):
                        print('calcula escorregamento')
                        escorregamento = float(self.input_escorregamento.text())
                        rpm_real = rpm-(((rpm/100)*escorregamento))
                        self.rpm_real.setText('RPM de Saida ~Real: '+str(rpm_real)+' [RPM]')
                        print('calcula rpm_real')
                        self.escorregamento.setText('Escorregamento [%]: ')
            except:
                print('erro ao converter input escorregamento para float')
                self.escorregamento.setText('Escorregamento [%]: Erro. entrada float : 0.0')

        # Calculate RPM after Reduction
        if self.input_reducao.text():
            try:
                if isinstance(float(self.input_reducao.text()),float):
                        reducao = float(self.input_reducao.text())
                        rpm_apos_reducao = rpm_real/reducao
                        self.rpm_apos_reducao.setText('RPM após Redução: '+str(rpm_apos_reducao)+' [RPM]')
                        print('calcula rpm apos reducao')
                        self.reducao.setText(
                            'Redução [1/X]: ')
            except:
                print('erro ao converter input reducao para float')
                self.reducao.setText(
                    'Redução [1/X]: Erro. entrada float : 0.0')

        # Calculate Cylinder Perimeter
        if self.input_diametro_de_tracao.text():
            try:
                if isinstance(float(self.input_diametro_de_tracao.text()),float):
                        diametro_de_tracao = float(self.input_diametro_de_tracao.text())
                        perimetro_do_cilindro = diametro_de_tracao*math.pi
                        self.perimetro_do_cilindro.setText(
                            'Perímetro do Cilindro de Tração [mm]: '
                            +str(perimetro_do_cilindro)+' [mm]'
                            )
                        print('calcula perimetro do cilindro')
                        self.diametro_do_cilindro.setText(
                            'Diâmetro do Cilindro de Tração [mm]: ')
            except:
                print('erro ao converter input_diametro_de_tracao para float')
                self.diametro_do_cilindro.setText(
                    'Diâmetro do Cilindro de Tração [mm]: Erro. entrada float : 0.0')
        
        # Cylinder tangent Velocity
        if perimetro_do_cilindro and rpm_apos_reducao:
            velodidade_tangente_m_min = (perimetro_do_cilindro*rpm_apos_reducao)/1000
            self.velocidade_tangente.setText(
                'Velocidade Tangente [m/min]: '
                +str(velodidade_tangente_m_min)+' [m/min]'
                )
            print('calcula velocidade linear do cilindro')

       
        # Pontência = (V*raiz3*FP*rendimento)*(( corrente A )*FS)

        # Tensão do motor        
        if self.input_tensao_do_motor.text():
            try:
                if isinstance(float(self.input_tensao_do_motor.text()),float):
                        tensao_do_motor = float(self.input_tensao_do_motor.text())
                        print('input tensão do motor')                       
            except:
                print('erro input tensão do motor')

        # FP
        if self.input_FP.text():
            try:
                if isinstance(float(self.input_FP.text()),float):
                        FP = float(self.input_FP.text())
                        print('input FP')                       
            except:
                print('erro input FP')

        # rendimento
        if self.input_rendimento.text():
            try:
                if isinstance(float(self.input_rendimento.text()),float):
                        rendimento = float(self.input_rendimento.text())
                        print('input rendimento do motor')                       
            except:
                print('erro input rendimento do motor')

        # Corrente A
        if self.input_corrente.text():
            try:
                if isinstance(float(self.input_corrente.text()),float):
                        corrente = float(self.input_corrente.text())
                        print('input corrente do motor')                       
            except:
                print('erro input corrente do motor')

        # FS
        if self.input_FS.text():
            try:
                if isinstance(float(self.input_FS.text()),float):
                        FS = float(self.input_FS.text())
                        print('input FS do motor')                       
            except:
                print('erro input FS do motor')
        

        # calcula Potência
        #Pontência_w = (V*raiz3*FP*rendimento)*(( corrente A )*FS)
        if tensao_do_motor and FP and rendimento and corrente and FS:
            potencia_w = (tensao_do_motor*(math.sqrt(3))*FP*rendimento)*corrente
            self.potencia_w.setText('Potência [W]: '+str(potencia_w)+ ' [w]')
            #Pontência_cv = Pontência_w / (735,499)
            self.potencia_cv.setText('Potência [CV]: '+str(potencia_w/735.499)+ ' [CV]')

        # conjugado kgfm = potencia_w / rpm_motor ~real
        if potencia_w and rpm_real:
            conjugado_kgmf = potencia_w/rpm_real
            self.conjugado_kgmf.setText('Conjugado [kgmf]: '+str(conjugado_kgmf)+' [kgfm]')

        # conjugado nominal [Nm] = potencia_w/( rpm_real*(2*pi)/60)
        if potencia_w and rpm_real:
            conjugado_nm = potencia_w/(rpm_real*(2.0*math.pi)/60.0)
            self.conjugado_nm.setText('Conjugado [Nm]: '+str(conjugado_nm)+'[Nm]')

        # Rendimento do redutor [%]
        if self.input_rendimento_redutor.text():
            try:
                if isinstance(float(self.input_rendimento_redutor.text()),float):
                        rendimento_redutor = float(self.input_rendimento_redutor.text())
                        print('input rendimento_redutor do motor')                       
            except:
                print('erro input rendimento_redutor do motor')

        # Torque após redutor [Nm] = ((conjugado_nm*reducao)/100)*rendimento
        if conjugado_nm and reducao and rendimento_redutor:
            torque_redutor = ((conjugado_nm*reducao)/100)*rendimento_redutor
            self.torque_redutor.setText(
                'Torque após redutor [Nm]: '+str(torque_redutor)+'[Nm]')

        # Força tangente ao cilindro [N] = torque_reduto / ((diametrodo_de_tracao/2)mm)metros
        if torque_redutor and diametro_de_tracao:
            forca_tangente = torque_redutor / ((diametro_de_tracao/2.0)/1000)
            self.forca_tagente.setText(
                'Força tangente ao cilindro [N]: '+str(forca_tangente)+'[Nm]')

        # Carga máxima tangente cilindro [kg] = forca_tangente / gravidade
        if forca_tangente and gravidade:
            carga_tangente = forca_tangente / gravidade
            self.carga_tagente.setText(
                'Carga máxima tangente cilindro [kg]: '
                +str(carga_tangente)+'[kg]')

        # Fim calcular_transporte
        
    def funcao_gerar_pdf(self):
        pdf = FPDF('P', 'mm', 'A4')
    
        print('Gerar PDF')
        timestamp = time.time()
        dt_object = datetime.fromtimestamp(timestamp)
        print('Data: ',dt_object)
        #pdf.cell(100, 10, txt = 'Data: '+ str(dt_object),ln = 1, align ='L')

        pdf.add_page()
        pdf.set_font('Arial', size = 12)
        pdf.cell(200, 10, txt = 'Máquina Configurada '+'Data: '+ str(dt_object),ln = 1, align ='C')
        pdf.cell(100, 5, txt = 'Cliente :',ln = 1, align ='L')
        pdf.cell(100, 5, txt = 'O.F. :',ln = 1, align ='L')
        pdf.cell(100, 5, txt = 'Quantidade :',ln = 1, align ='L')

        if self.input_frequencia.text():
            pdf.add_page()
            pdf.set_font('Arial', size = 12)
            pdf.cell(200, 10, txt = 'Cálculos executados '+'Data: '+ str(dt_object),ln = 1, align ='C')
            pdf.cell(100, 5, txt = 'Cliente :',ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'O.F. :',ln = 1, align ='L')
            pdf.cell(100, 10, txt = 'Cálculos de Transporte',ln = 1, align ='C')

            # Velocidade do motor        
            pdf.cell(100, 10, txt = 'Velocidade do Motor',ln = 1, align ='L')
            #print('frequencia [Hz]: ',self.input_frequencia.text())
            pdf.cell(100, 5, txt = 'Frequência [Hz]: '+ str(self.input_frequencia.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Polos [Hz]: '+ str(self.input_polos.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.rpm.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Escorregamento [%]: '+ str(self.input_escorregamento.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.rpm_real.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Redução [1/x]: 1/'+ str(self.input_reducao.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.rpm_apos_reducao.text()),ln = 1, align ='L')
            
            # Velocidade do Cilindro      
            pdf.cell(100, 10, txt = 'Velocidade do Cilindro',ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Diâmetro do Cilindro [mm]: '+ str(self.input_diametro_de_tracao.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.velocidade_tangente.text()),ln = 1, align ='L')

            # Torque do motor
            pdf.cell(100, 10, txt = 'Torque do Motor',ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Tensão do Motor [V]: '+ str(self.input_tensao_do_motor.text())+' V',ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Fator de Potência [FP]: '+ str(self.input_FP.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Rendimento [n]: '+ str(self.input_rendimento.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Corrente [A]: '+ str(self.input_corrente.text())+' A',ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Fator de Serviço [FS]: '+ str(self.input_FS.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.potencia_cv.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.potencia_w.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.conjugado_kgmf.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.conjugado_nm.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = 'Rendimento do Redutor [%]: '+ str(self.input_rendimento_redutor.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.torque_redutor.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.forca_tagente.text()),ln = 1, align ='L')
            pdf.cell(100, 5, txt = str(self.carga_tagente.text()),ln = 1, align ='L')
        else:
            print('Cálculos de Transporte entrada de frequência vazia')

        file_name = QFileDialog.getSaveFileName(self, 'Save File','Maquina_configurada.pdf',filter='Arquivo(*.pdf)')
        print('file_name: ', file_name[0])
        if file_name[0]:
            pdf.output(file_name[0],dest='F').encode('latin-1')
        else:
            print('erro_arquivo_sem_nome')

    def confirma_saida(self):
        confirma = QMessageBox.question(self,
        #confirma = QMessageBox.critical(self,
                                        'Atenção',
                                        'Dados não salvos serão perdidos, Deseja mesmo sair?',
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
                                         "Atenção",
                                         "Dados não salvos serão perdidos, Deseja mesmo sair?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
app.setStyleSheet('.QLabel { font-size: 11pt;} .QLineEdit { font-size: 11pt;}')
sys.exit(qt.exec())