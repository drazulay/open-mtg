import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QMenuBar,
    QToolBar,
    QAction,
    QStatusBar
)


class OMApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.setWindowIcon(QIcon("../../data/images/icon.png"))


class OMWindow(QMainWindow):
    title = ""

    def __init__(self):
        super().__init__()

        self.setGeometry(400, 200, 1024, 600)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        self.button_duel = QAction("Duel", self)
        self.button_duel.setStatusTip("Start a duel")
        self.button_duel.triggered.connect(self.handleDuelBtnClick)
        self.button_duel.setIcon(QIcon("../../data/images/btn_duel.png"))
        self.button_duel.setIconVisibleInMenu(True)
        toolbar.addAction(self.button_duel)

        self.button_settings = QAction("Settings", self)
        self.button_settings.setStatusTip("Start a settings")
        self.button_settings.triggered.connect(self.handleSettingsBtnClick)
        self.button_settings.setIcon(QIcon("../../data/images/btn_settings.png"))
        self.button_settings.setIconVisibleInMenu(True)
        toolbar.addAction(self.button_settings)

        self.label = QLabel(self.title)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.setStatusBar(QStatusBar(self))

    def handleDuelBtnClick(self, s):
        self.label.setText("Duel")

    def handleSettingsBtnClick(self, s):
        self.label.setText("Settings")


if __name__ == '__main__':
    app = OMApp(sys.argv)
    window = OMWindow()
    window.setWindowTitle("Open MTG")

    window.setFixedWidth(1024)
    window.setFixedHeight(768)
    window.show()
    app.exec()

