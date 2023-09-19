import cv2 as cv
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QLinearGradient, QColor, QPainter
from .camerawindow import CameraWindow

from PySide6.QtWidgets import (
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel,
    QSlider,
    QLineEdit,
    QPushButton
)

from ..transform.train_model_regressor import TrainModelRegressor
from ..transform.transform import Transform

class TemplateLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Define Camera
        self.camera = CameraWindow()

        # Define a font size 
        font = QFont() 
        font.setPointSize(14)
        font.setBold(True)

        # Temperature Indicator
        self.temp_label = QLabel("CCT Correlation Color Temperature [Kelvin]:")
        self.temp_label.setFont(font)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.temp_box = QLineEdit()
        self.temp_box.setFixedSize(200, 50)
        self.temp_box.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.temp_box.setReadOnly(True)
        self.temp_box.setFont(font)

        self.temp_box_layout = QHBoxLayout()
        self.temp_box_layout.setSpacing(10)
        self.temp_box_layout.addWidget(self.temp_box)
        self.temp_box_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Label Slider
        self.color_temp_label = QLabel("Color Temperature Scale")
        self.color_temp_label.setFont(font)
        self.color_temp_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.start_label = QLabel("1.000")
        self.start_label.setFont(font)
        self.start_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.start_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.end_label = QLabel("10.000")
        self.end_label.setFont(font)
        self.end_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.end_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # border_style = "border: 2px solid white;"
        # start_label.setStyleSheet(border_style)
        # end_label.setStyleSheet(border_style)

        self.slider_layout = QHBoxLayout()
        self.label_layout = QHBoxLayout()

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1000)
        self.slider.setMaximum(10000)
        self.slider.setSingleStep(200)
        self.slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.slider.setTickInterval(200)
        self.slider.setFixedSize(550,70)
        self.slider.setStyleSheet(
        """
            QSlider {
                background: 
                qlineargradient(
                    x1:0, y1:0, 
                    x2:0.8, y2:0
                    x3:0.8, y3:0
                    x4:1, y4:0
                    stop: 0 #ff3300, 
                    stop: 0.6 #ffcb8d, 
                    stop: 0.8 #fff9fd, 
                    stop: 1 #cfdaff);

                    height: 20px;
            }
        """
        )

        # Layout Slider -> startlabel - Slider - endlabel
        self.slider_layout.addWidget(self.start_label)
        self.slider_layout.addWidget(self.slider)
        self.slider_layout.addWidget(self.end_label)
        self.label_layout.addWidget(self.start_label)
        self.label_layout.addWidget(self.end_label)

        # Button Calculate Temp
        font_button = QFont() 
        font_button.setPointSize(12)
        font_button.setBold(True)

        self.button_capture_temp = QPushButton("Capture ColorTemperature")
        self.button_capture_temp.setFixedSize(300, 70)
        self.button_capture_temp.setFont(font_button)
        self.button_capture_temp.setStyleSheet("color: default;")

        self.button_aplly = QPushButton("Preview")
        self.button_aplly.setFixedSize(300, 70)
        self.button_aplly.setFont(font_button)
        self.button_aplly.setStyleSheet("color: default;")

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_capture_temp)
        self.button_layout.addWidget(self.button_aplly)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Add Wigets
        self.addWidget(self.temp_label)
        self.addLayout(self.temp_box_layout)
        self.addWidget(self.camera)
        self.addWidget(self.color_temp_label)
        self.addLayout(self.slider_layout)
        self.addLayout(self.label_layout)
        self.addLayout(self.button_layout)

        # Connect Wigets Callback
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.button_capture_temp.clicked.connect(self.capture_temperature_image)
    
    def slider_value_changed(self, value):
        self.temp_box.setText(str(value))
        temperature = value
        print(f"Temperature: {temperature} K")

    def calculate_slider_value(self, temperature):
        # Calculate the slider value based on the temperature
        # Modify this calculation according to your needs
        slider_value = temperature
        return slider_value
    
    def calculate_color_temperature(self, frame):
        """
        """
        transform = Transform(frame=frame)
        img_temp = transform.BGR2TEMP().reshape(-1, 1)
        return img_temp.min()

    def capture_temperature_image(self):
        filename = f"./resources/tmp/img.jpg" 

        # Capture the current frame from the camera
        ret, frame = self.camera.camera.read()

        if ret:
            # Save the frame as a JPEG image
            cv.imwrite(filename, frame)
            color_temperature = self.calculate_color_temperature(frame)

            # Calculate the slider value based on the color temperature
            slider_value = self.calculate_slider_value(color_temperature)

            # Update the slider value
            self.slider.setValue(slider_value)
    