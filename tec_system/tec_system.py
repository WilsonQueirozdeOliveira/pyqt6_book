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
        self.setGeometry(0,30,680,690)
        self.Interface()
        
    def Interface(self):
        layout = QVBoxLayout()

        self.tabs = QTabWidget()

        # tab1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, 'Configurar máquina')
        layout_tab1 = QHBoxLayout()

        # tab2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, 'Cálculos de transporte')
        layout_tab2 = QHBoxLayout()

        # Imput column 0 tab2
        layout_input_column_0_tab2 = QVBoxLayout()
        # Title
        velocidade_do_motor = QLabel('Velocidade do motor:')
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
        velocidade_da_reducao = QLabel('Velociadade da redução:')
        layout_input_column_0_tab2.addWidget(velocidade_da_reducao)

        # Reduction
        layout_reducao = QHBoxLayout()
        reducao = QLabel('Redução [1/X]: ')
        layout_reducao.addWidget(reducao)
        self.input_reducao = QLineEdit(self)
        self.input_reducao.setPlaceholderText('X')
        layout_reducao.addWidget(self.input_reducao)
        layout_input_column_0_tab2.addLayout(layout_reducao)

        # RPM after Reduction
        rpm_reducao = QLabel('RPM após Redução: ')
        layout_input_column_0_tab2.addWidget(rpm_reducao)

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
        
        velocidade_do_motor = QLabel('coluna2:')
        layout_input_column_1_tab2.addWidget(velocidade_do_motor)
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
        self.tabs.addTab(self.tab3, 'sobre')
        layout_tab3 = QHBoxLayout()

        layout.addWidget(self.tabs)

        self.tab1.setLayout(layout_tab1)
        self.tab2.setLayout(layout_tab2)
        self.tab3.setLayout(layout_tab3)

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