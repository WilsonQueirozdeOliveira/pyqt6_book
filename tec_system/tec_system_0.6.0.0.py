import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QScrollArea, QLabel

class ScrollViewExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scroll View Example')
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title Tec System
        Title_Tec_System = QLabel()
        Title_Tec_System.setText("Tec_System\n")  # Create Title

        # Add the Title to the central layout
        layout.addWidget(Title_Tec_System)

        # Create a QTextEdit widget to put inside the scroll view
        #text_edit = QTextEdit()
        text_edit = QLabel()
        text_edit.setText("This is some text that will be scrollable.\n" * 20)  # Create a long text

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidget(text_edit)
        scroll_area.setWidgetResizable(True)  # Make the widget inside the scroll area resizable

        # Add the scroll area to the central layout
        layout.addWidget(scroll_area)

def main():
    app = QApplication(sys.argv)
    window = ScrollViewExample()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
