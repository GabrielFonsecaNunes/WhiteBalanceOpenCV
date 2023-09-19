import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene 

class HistogramWindow(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image
        
        layout = QVBoxLayout()
        self.image_label = QLabel("RGB Histogram", self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.update_histogram()
        
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def update_histogram(self):
        histogram_rgb = cv.cvtColor(self.histogram(image=self.image), cv.COLOR_BGR2RGB)
        h, w, ch = histogram_rgb.shape
        Qimage = QImage(histogram_rgb.data, w, h, ch * w, QImage.Format_RGB888)# type: ignore
        pixmap = QPixmap.fromImage(Qimage)
        self.image_label.setPixmap(pixmap)

    def histogram(self, image):
        """
        """
        plt.title("Histograma RGB")
        plt.figure(figsize= (15, 8))
        color = ('b','g','r')

        for i,col in enumerate(color):
            histr = cv.calcHist([image],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])

        plt.plot(data = image)
        plt.xlabel('Valor do Pixel')
        plt.ylabel('Frequência')
        plt.legend(['R', 'G', 'B'])

        histogram_image_path = './resources/graphics/histogram.png'
        plt.savefig(histogram_image_path)

        histogram_image = cv.imread(histogram_image_path)
        return histogram_image