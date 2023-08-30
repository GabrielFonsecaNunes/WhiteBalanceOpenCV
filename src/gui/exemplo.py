from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        label = QLabel("Segunda Tela")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Crie um item de menu
        self.second_window = None  # Mantenha uma referência para a segunda tela
        second_window_action = QAction("Mostrar Segunda Tela", self)
        second_window_action.triggered.connect(self.show_second_window)
        
        # Adicione o item de menu à barra de menu
        menu = self.menuBar()
        file_menu = menu.addMenu("Arquivo")
        file_menu.addAction(second_window_action)
        
    def show_second_window(self):
        if not self.second_window:
            self.second_window = SecondWindow()
            self.second_window.setWindowTitle("Segunda Tela")
            self.second_window.setGeometry(100, 100, 400, 300)  # Defina a geometria da janela
        self.second_window.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
