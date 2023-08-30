from .template_layout import TemplateLayout
from .graphics import HistogramWindow
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
        QApplication, 
        QMainWindow, 
        QWidget,
        QPushButton
)
# theme dark
import cv2 as cv
import numpy as np
from qdarktheme import load_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define Title Window
        self.setWindowTitle("WizardVideo - WhiteBalance")
        self.histogram_window = None  # Mantenha uma referência para a segunda tela

        # Define Menu
        menu = self.menuBar()
        view = menu.addMenu("View")

        mask_filter = QAction("Mask Regions Greater Illumination Pixels White", self)
        view.addAction(mask_filter)
        graphics_menu = menu.addMenu("Graphics")
        graphics_histogram_action = QAction("RGB Histogram", self)
        graphics_histogram_action.triggered.connect(self.histogram_window)
        graphics_menu.addAction(graphics_histogram_action)

        # Define Layout () 
        layout = TemplateLayout()
        # layout.setSpacing(20)

        graphics_histogram_action.triggered.connect(self.show_rgb_histogram)

        # Put components in layout
        base = QWidget()
        base.setLayout(layout)
        base.setFixedSize(720, 800)
        self.setCentralWidget(base)

    def show_rgb_histogram(self):
        # Capture the current frame from the camera
        path_img = "./resources/tmp/img.jpg"
        img = cv.imread(path_img)

        # Create a histogram window and show it
        if not self.histogram_window:
            self.histogram_window = HistogramWindow(img)
            self.histogram_window.setWindowTitle("Segunda Tela")
            self.histogram_window.setGeometry(100, 100, 400, 300)  # Defina a geometria da janela
        self.histogram_window.show()

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(load_stylesheet("light"))
    window = MainWindow()
    window.show()
    app.exec()