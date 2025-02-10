import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from src.sparcle_ui import SparcleMainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sparcle")
    app.setWindowIcon(QIcon('assets/sparcle_icon.ico'))
    
    window = SparcleMainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 