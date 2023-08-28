from camerawindow import CameraWindow
from PySide6.QtCore import Qt
from template_layout import TemplateLayout
from PySide6.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget
)
# theme dark
from qdarktheme import load_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define Title Window
        self.setWindowTitle("WizardVideo - WhiteBalance")

        # Define Menu
        menu = self.menuBar()
        menu.addMenu("File")
        menu.addMenu("View")
        menu.addMenu("Graphics")
        menu.addMenu("Help")

        # Define Layout () 
        layout = TemplateLayout()

        # Put components in layout
        base = QWidget()
        base.setLayout(layout)
        base.setFixedSize(720, 480)
        self.setCentralWidget(base)
        
if __name__ == '__main__':
    app = QApplication([])
    # app.setStyleSheet(load_stylesheet())
    window = MainWindow()
    window.show()
    app.exec()