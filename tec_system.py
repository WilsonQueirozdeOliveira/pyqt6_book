import sys

print(sys.version)

import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema')
        self.setWindowIcon(QIcon('logo_wilson_eletrica.jpg'))
        self.setGeometry(150, 80, 1000, 600)
        
        self.show()
        
        
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())