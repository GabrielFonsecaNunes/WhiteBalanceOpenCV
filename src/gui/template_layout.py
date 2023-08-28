from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QLinearGradient, QColor, QPainter
from camerawindow import CameraWindow
from PySide6.QtWidgets import (
    QVBoxLayout, 
    QHBoxLayout, 
    QSpacerItem, 
    QSizePolicy, 
    QLabel,
    QSlider
)

class TemplateLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Define Camera
        camera_widget = CameraWindow()

        # Define a font size 
        font = QFont() 
        font.setPointSize(16) 

        # Label Slider
        start_label = QLabel("1.000")
        start_label.setFont(font)
        start_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        start_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        end_label = QLabel("10.000")
        end_label.setFont(font)
        end_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        end_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # border_style = "border: 2px solid white;"
        # start_label.setStyleSheet(border_style)
        # end_label.setStyleSheet(border_style)

        slider_layout = QHBoxLayout()
        label_layout = QHBoxLayout()


        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(1000)
        slider.setMaximum(10000)
        slider.setSingleStep(200)
        slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        slider.setTickInterval(200)
        slider.setFixedSize(550, 80)
        slider.setStyleSheet(
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

        spacer_left = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum) # type: ignore
        spacer_right = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum) # type: ignore

        slider_layout.addWidget(start_label)
        slider_layout.addWidget(slider)
        slider_layout.addWidget(end_label)
        label_layout.addWidget(start_label)
        label_layout.addWidget(end_label)

        # Add Wigets
        self.addWidget(camera_widget)
        self.addLayout(slider_layout)
        self.addLayout(label_layout)

        # Connect Wigets Callback
        slider.valueChanged.connect(self.slider_value_changed)
    
    def slider_value_changed(self, value):
        temperature = value
        print(f"Temperature: {temperature} K")
