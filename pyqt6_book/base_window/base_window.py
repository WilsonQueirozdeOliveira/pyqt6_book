import sys

print(sys.version)

import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('base_window')
        self.setWindowIcon(QIcon('python.png'))
        self.setGeometry(150, 80, 1000, 600)
        
        self.show()
        
        
qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())