from ast import arguments
from cmath import pi
from re import S
import sys 
import math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Automação de cálculos de Dimensionamento')
        #self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(0,30,680,690)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()

        self.tabs = QTabWidget()

        # tab1
        self.tab1 = QWidget()
        #self.tabs.addTab(self.tab1, 'Configurar máquina')
        layout_tab1 = QHBoxLayout()

        # tab2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, 'Cálculos de transporte')
        layout_tab2 = QHBoxLayout()

        # Imput column 0 tab2
        layout_input_column_0_tab2 = QVBoxLayout()
        # Title
        velocidade_do_motor = QLabel('Velocidade do Motor')
        velocidade_do_motor.setStyleSheet("QLabel { color : blue; }")
        layout_input_column_0_tab2.addWidget(velocidade_do_motor)
        
        #frequency
        layout_frequencia = QHBoxLayout()
        self.frequencia = QLabel('Frequência [Hz]:')
        #layout_input_column_0_tab2.addWidget(self.frequencia)
        layout_frequencia.addWidget(self.frequencia)
        self.input_frequencia = QLineEdit(self)
        self.input_frequencia.setPlaceholderText('Hz')
        self.input_frequencia.textChanged.connect(self.calcular)
        #layout_input_column_0_tab2.addWidget(self.input_frequencia)
        layout_frequencia.addWidget(self.input_frequencia)
        layout_input_column_0_tab2.addLayout(layout_frequencia)
        
        # Poles
        layout_polos = QHBoxLayout()
        self.polos = QLabel('Polos [Nº]:')
        #layout_input_column_0_tab2.addWidget(self.polos)
        layout_polos.addWidget(self.polos)
        self.input_polos = QLineEdit(self)
        self.input_polos.setPlaceholderText('Nº(2-4-8-16)')
        self.input_polos.textChanged.connect(self.calcular)
        #layout_input_column_0_tab2.addWidget(self.input_polos)
        layout_polos.addWidget(self.input_polos)
        layout_input_column_0_tab2.addLayout(layout_polos)

        # Pear fo poles
        self.par_de_polos = QLabel('Par de Polos [Nº]: ')
        layout_input_column_0_tab2.addWidget(self.par_de_polos)
        
        self.rps = QLabel('RPS:')
        layout_input_column_0_tab2.addWidget(self.rps)

        # RPM
        self.rpm = QLabel('RPM:')
        layout_input_column_0_tab2.addWidget(self.rpm)

        #slip
        layout_escoregamento = QHBoxLayout()
        self.escoregamento = QLabel('Escoregamento [%]:')
        #layout_input_column_0_tab2.addWidget(self.escoregamento)
        layout_escoregamento.addWidget(self.escoregamento)
        self.input_escoregamento = QLineEdit(self)
        self.input_escoregamento.setPlaceholderText('0.0%')
        self.input_escoregamento.textChanged.connect(self.calcular)
        #layout_input_column_0_tab2.addWidget(self.input_escoregamento)
        layout_escoregamento.addWidget(self.input_escoregamento)
        layout_input_column_0_tab2.addLayout(layout_escoregamento)

        # RPM ~Real
        self.rpm_real = QLabel('RPM de Saida ~Real: ')
        layout_input_column_0_tab2.addWidget(self.rpm_real)

        # Reduction velocity
        velocidade_da_reducao = QLabel('Velociadade da redução')
        velocidade_da_reducao.setStyleSheet("QLabel { color : blue; }")
        layout_input_column_0_tab2.addWidget(velocidade_da_reducao)

        # Reduction
        layout_reducao = QHBoxLayout()
        self.reducao = QLabel('Redução [1/X]: ')
        layout_reducao.addWidget(self.reducao)
        self.input_reducao = QLineEdit(self)
        self.input_reducao.setPlaceholderText('X')
        layout_reducao.addWidget(self.input_reducao)
        self.input_reducao.textChanged.connect(self.calcular)
        layout_input_column_0_tab2.addLayout(layout_reducao)

        # RPM after Reduction
        self.rpm_apos_reducao = QLabel('RPM após Redução: ')
        layout_input_column_0_tab2.addWidget(self.rpm_apos_reducao)

        # Cylinder velocity
        velocidade_do_cilindro = QLabel('Velociadade do Cilindro')
        #velocidade_do_cilindro.setStyleSheet("QLabel { background-color : red; color : blue; }")
        velocidade_do_cilindro.setStyleSheet("QLabel { color : blue; }")
        layout_input_column_0_tab2.addWidget(velocidade_do_cilindro)

        # traction diameter 
        layout_diametro_de_tracao = QHBoxLayout()
        self.diametro_do_tambor = QLabel('Diâmetro do Cilindro de Tração [mm]:')
        layout_diametro_de_tracao.addWidget(self.diametro_do_tambor)
        self.input_diametro_de_tracao = QLineEdit(self)
        self.input_diametro_de_tracao.setPlaceholderText('0.0 mm')
        layout_diametro_de_tracao.addWidget(self.input_diametro_de_tracao)
        self.input_diametro_de_tracao.textChanged.connect(self.calcular)
        layout_input_column_0_tab2.addLayout(layout_diametro_de_tracao)

        # Cylinder Perimeter
        self.perimetro_do_cilindro = QLabel(
            'Perímetro do Cilindro de Tração [mm]: ')
        layout_input_column_0_tab2.addWidget(self.perimetro_do_cilindro)

        # Cylinder linear Velocity
        self.velocidade_linear = QLabel(
            'Velocidade Linear [m/min]: ')
        layout_input_column_0_tab2.addWidget(self.velocidade_linear)




        # Functions
        '''
        funcoes = QLabel('Funções:')
        layout_input_column_0_tab2.addWidget(funcoes)
        funcao_1 = QLabel('Par de polos = Polos / 2')
        layout_input_column_0_tab2.addWidget(funcao_1)
        funcao_2 = QLabel('RPS = Frequência / ( Par de polos )')
        layout_input_column_0_tab2.addWidget(funcao_2)
        funcao_3 = QLabel('RPM = RPS * 60[s]')
        layout_input_column_0_tab2.addWidget(funcao_3)
        funcao_4 = QLabel('RPM ~Real = RPM - Escoregamento [%]')
        layout_input_column_0_tab2.addWidget(funcao_4)
        '''

        layout_input_column_0_tab2.addStretch()

        layout_tab2.addLayout(layout_input_column_0_tab2)

        # Imput column 1 tab2
        layout_input_column_1_tab2 = QVBoxLayout()
        
        # Engine Torque
        torque_do_motor = QLabel('Torque do Motor')
        torque_do_motor.setStyleSheet("QLabel { color : blue; }")
        layout_input_column_1_tab2.addWidget(torque_do_motor)

        frequencia = QLabel('coluna2:')
        layout_input_column_1_tab2.addWidget(frequencia)
        input_frequencia = QLineEdit(self)
        input_frequencia.setPlaceholderText('coluna2')
        layout_input_column_1_tab2.addWidget(input_frequencia)
        layout_input_column_1_tab2.addStretch()

        layout_tab2.addLayout(layout_input_column_1_tab2)
        layout_tab2.addStretch()
        
        # tab3
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, 'Calculos de produtividade')
        layout_tab3 = QHBoxLayout()

        # tab4
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4, 'sobre')
        layout_tab4 = QHBoxLayout()

        layout.addWidget(self.tabs)

        self.tab1.setLayout(layout_tab1)
        self.tab2.setLayout(layout_tab2)
        self.tab3.setLayout(layout_tab3)
        self.tab3.setLayout(layout_tab4)

        botao_sair = QPushButton('SAIR', self)
        #botao0.move(275,260)
        botao_sair.clicked.connect(self.confirma_saida)

        layout_botoes_inferiores = QHBoxLayout()
        
        layout.addLayout(layout_botoes_inferiores)

        layout_botoes_inferiores.addStretch()
        layout_botoes_inferiores.addWidget(botao_sair)

        self.setLayout(layout)

        self.show()

    def novo(self):
        print('Novo projeto criado com sucesso.')

    def calcular(self):
        print(self.input_frequencia.text())
        print(self.input_polos.text())
        print(self.rps.text())

        input_polos = 0
        par_de_polos = 0
        rpm = 0
        escorregamento =0
        rpm_real = 0
        rpm_apos_reducao = 0
        perimetro_do_cilindro = 0
        
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
                print('erro ao converter input_polos para float')
                self.polos.setText('Polos [Nº]: Erro. Erro entrada float : 0.0')

        # Calculate RPM
        if self.input_frequencia.text():
            try:
                if isinstance(float(self.input_frequencia.text()),float) and par_de_polos:
                    frequencia = int(self.input_frequencia.text())
                    self.rps.setText('RPS: '+str(frequencia/par_de_polos))
                    rpm = (frequencia/par_de_polos)*60
                    self.rpm.setText('RPM: '+str(rpm)+' Sem escorregamento.')
                    print('calcula rpm')
                    self.frequencia.setText('Frequência [Hz]:')
            except:
                print('erro ao converter input_frequencia para float')
                self.frequencia.setText('Frequência[Hz]: Erro. entrada float : 0.0')

        # Calculate ~Real RPM
        if self.input_escoregamento.text():
            try:
                if isinstance(float(self.input_escoregamento.text()),float):
                        print('calcula escorregamento')
                        escorregamento = float(self.input_escoregamento.text())
                        rpm_real = rpm-(((rpm/100)*escorregamento))
                        self.rpm_real.setText('RPM de Saida ~Real: '+str(rpm_real)+' [RPM]')
                        print('calcula rpm_real')
                        self.escoregamento.setText('Escoregamento [%]: ')
            except:
                print('erro ao converter input_escorregamento para float')
                self.escoregamento.setText('Escoregamento [%]: Erro. entrada float : 0.0')

        # Calculate RPM after Reduction
        if self.input_reducao.text():
            try:
                if isinstance(float(self.input_reducao.text()),float):
                        reducao = float(self.input_reducao.text())
                        rpm_apos_reducao = rpm_real/reducao
                        self.rpm_apos_reducao.setText('RPM após Redução: '+str(rpm_apos_reducao)+' [RPM]')
                        print('calcula rpm_apos_reducao')
                        self.reducao.setText(
                            'Redução [1/X]: ')
            except:
                print('erro ao converter input_reducao para float')
                self.reducao.setText(
                    'Redução [1/X]: Erro. entrada float : 0.0')

        # Calculate Cylinder Perimeter
        if self.input_diametro_de_tracao.text():
            try:
                if isinstance(float(self.input_diametro_de_tracao.text()),float):
                        raio_de_tracao = float(self.input_diametro_de_tracao.text())
                        perimetro_do_cilindro = raio_de_tracao*pi
                        self.perimetro_do_cilindro.setText(
                            'Perímetro do Cilindro de Tração [mm]: '
                            +str(perimetro_do_cilindro)+' [mm]'
                            )
                        print('calcula perimetro_do_cilindro')
                        self.diametro_do_tambor.setText(
                            'Diâmetro do Cilindro de Tração [mm]: ')
            except:
                print(
                    'erro ao converter input_raio_de_tracao para float')
                self.diametro_do_tambor.setText(
                    'Diâmetro do Cilindro de Tração [mm]: Erro. entrada float : 0.0')
        
        # Cylinder linear Velocity
        if perimetro_do_cilindro and rpm_apos_reducao:
            velodidade_linear_m_min = (perimetro_do_cilindro*rpm_apos_reducao)/1000
            self.velocidade_linear.setText(
                'Velocidade linear [m/min]: '
                +str(velodidade_linear_m_min)+' [m/min]'
                )
            print('calcula Cylinder linear Velocity')



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
app.setStyleSheet('.QLabel { font-size: 13pt;} .QLineEdit { font-size: 13pt;}')
sys.exit(qt.exec())