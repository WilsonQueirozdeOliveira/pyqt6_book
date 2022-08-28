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
        self.setGeometry(150,150,365,300)
        self.Interface()
       
    def Interface(self):

        texto_slider = QLabel('Quanto de mimória deseja alocar?',self)
        texto_slider.move(10,20)
        self.slider = QSlider(Qt.Orientation.Horizontal,self)
        self.slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.slider.setGeometry(10,40,330,30)
        self.slider.setMinimum(20)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.recebe_valor)
        self.valor = QLabel('0')
        self.valor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao1 = QPushButton('SAIR', self)
        botao1.move(275,260)
        botao1.clicked.connect(self.confirma_saida)

        self.show()

    def recebe_valor(self):
        val_escolhido = self.slider.value()
        self.valor.setText(str(val_escolhido))
        print(f'Valor escolhido:{val_escolhido}%')
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