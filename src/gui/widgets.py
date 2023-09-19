# widgets.py
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("MyWidget")

        # Define the logic for the widget
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("You clicked the button!")

