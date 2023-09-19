from src.gui.mainwindow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from src.transform.transform import TrainModelRegressor
from qdarktheme import load_stylesheet

if __name__ == "__main__":
    app = QApplication([])
    # app.setStyleSheet(load_stylesheet("light"))
    # icon = QIcon("./resources/icon/icon.jpg")
    # app.setWindowIcon(icon)
    window = MainWindow()
    window.show()
    app.exec()
