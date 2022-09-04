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
        self.setGeometry(150,150,500,400)
        self.Interface()
        
    def Interface(self):
        layout = QFormLayout()
        
        self.tabela = QTableWidget()
        self.tabela.setRowCount(10)
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderItem(0, QTableWidgetItem('Nome'))
        self.tabela.setHorizontalHeaderItem(1, QTableWidgetItem('Idade'))
        self.tabela.setHorizontalHeaderItem(2, QTableWidgetItem('Telefone'))
        self.tabela.setHorizontalHeaderItem(3, QTableWidgetItem('E-mail'))

        #self.tabela.horizontalHeader().hide()
        #self.tabela.verticalHeader().hide()

        self.tabela.setItem(0, 0, QTableWidgetItem('Fernado'))
        self.tabela.setItem(0, 1, QTableWidgetItem('34'))
        self.tabela.setItem(0, 2, QTableWidgetItem('55991357259'))
        self.tabela.setItem(0, 3, QTableWidgetItem('fernado2rad@gmail.com'))
        self.tabela.setItem(2, 0, QTableWidgetItem('Maria'))

        #bloquear edição
        #self.tabela.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.tabela.doubleClicked.connect(self.instancia_elemento)

        botao0 = QPushButton('SAIR', self)
        #botao0.move(275,260)
        botao0.clicked.connect(self.confirma_saida)
        botao1 = QPushButton('Salvar', self)
        botao1.clicked.connect(self.salva_dados)

        layout_buttons = QHBoxLayout()
        layout_buttons.addStretch()
        layout_buttons.addWidget(botao1)
        layout_buttons.addWidget(botao0)
        layout_buttons.addStretch()

        layout.addWidget(self.tabela)
        layout.addRow(layout_buttons)

        self.setLayout(layout)
        self.show()

    def salva_dados(self):
        base = []
        for dado in self.tabela.selectedItems():
            base.append(dado)

            print(f'O elemento {dado.text()} está localizado na linha {dado.row()} e na coluna {dado.column()}')
        pass

    def instancia_elemento(self):
        for dado in self.tabela.selectedItems():
            print(f'O elemento {dado.text()} está localizado na linha {dado.row()} e na coluna {dado.column()}')

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
      
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())