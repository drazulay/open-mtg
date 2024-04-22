import sys

from events import EventEmitter, EventType
from game import Game, Player, EventLoop

from OpenGL.GL import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import QGLWidget


class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 1024, 600)
        self.setBaseSize(1024, 600)
        self.setMinimumSize(1024, 600)
        self.setContentsMargins(0, 0, 0, 0)

    def initializeGL(self):
        print("Initializing OpenGL")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.textureId = self.bindTexture(
            QImage("../../data/images/background.png"),
            GL_TEXTURE_2D, GL_RGBA)

        print("Texture ID", self.textureId)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 1024, 600,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, [0] * 1024 * 600 * 4)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        glEnable(GL_TEXTURE_2D)
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.5)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

        glEnable(GL_LIGHTING)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.9, 0.9, 0.9, 1.0])
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    def resizeGL(self, w, h):
        self.makeCurrent()

        m_width = w
        m_height = h
        m_zoomFactor = 1.0

        if h == 0:
            h = 1

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glOrtho(0, m_width / m_zoomFactor, m_height / m_zoomFactor, 0,
                -1, 1);

    def paintGL(self):
        print("Drawing Pre-Match Screen")
        self.makeCurrent()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D, self.textureId)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(100.0, 100.0)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(300.0, 100.0)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(300.0, 300.0)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(100.0, 300.0)
        glEnd()

    def drawPreMatchScreen(self):
        pass


class GLWindow(QWidget):
    def __init__(self, event_emitter, screen=None, parent=None):
        super().__init__(parent)

        self.event_emitter = event_emitter

        rect = screen.availableGeometry()

        self.setWindowTitle("Open MTG")
        self.setGeometry(int(rect.width() / 4), int(rect.height() / 4), 1024,
                         600)
        self.setMinimumSize(1024, 600)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setGeometry(QRect(0, 0, 1024, 600))
        self.toolbar = QToolBar()
        self.glWidget = GLWidget()
        self.layout.addWidget(self.glWidget)
        self.layout.addWidget(self.toolbar)

        self.toolbar_buttons = {}

        self.btn_duel = QPushButton("Duel")
        self.btn_duel.clicked.connect(self.duel)
        self.btn_duel.setToolTip("Start a Duel")
        self.btn_duel.setShortcut("Ctrl+D")
        self.btn_duel.setIcon(QIcon("../../data/images/btn_duel.png"))
        self.toolbar.addWidget(self.btn_duel)
        self.toolbar_buttons['duel'] = self.btn_duel

        self.btn_decks = QPushButton("Deck Builder")
        self.btn_decks.clicked.connect(self.decks)
        self.btn_decks.setToolTip("Build out your Decks")
        self.btn_decks.setShortcut("Ctrl+B")
        self.btn_decks.setIcon(QIcon("../../data/images/btn_duel.png"))
        self.toolbar.addWidget(self.btn_decks)
        self.toolbar_buttons['decks'] = self.btn_decks

        self.btn_config = QPushButton("Config")
        self.btn_config.clicked.connect(self.config)
        self.btn_config.setToolTip("Game Configuration")
        self.btn_config.setShortcut("Ctrl+C")
        self.btn_config.setIcon(QIcon("../../data/images/btn_settings.png"))
        self.toolbar.addWidget(self.btn_config)
        self.toolbar_buttons['config'] = self.btn_config

        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(self.exit)
        self.btn_exit.setToolTip("Exit to Desktop")
        self.btn_exit.setShortcut("Ctrl+E")
        self.btn_exit.setIcon(QIcon("../../data/images/btn_settings.png"))
        self.toolbar.addWidget(self.btn_exit)
        self.toolbar_buttons['exit'] = self.btn_exit

        self.setLayout(self.layout)

    def duel(self):
        self.toolbar_buttons['duel'].setFocus()
        self.glWidget.drawPreMatchScreen()
        self.event_emitter.emit(EventType.E_GAME_START)
        print("Start a Duel")

    def decks(self):
        self.toolbar_buttons['decks'].setFocus()
        print("Build your Decks")

    def config(self):
        self.toolbar_buttons['config'].setFocus()
        print("Game Configuration")

    def closeEvent(self, a0, QCloseEvent=None):
        self.exit()

    def exit(self):
        self.toolbar_buttons['exit'].setFocus()
        dlg = QDialog()

        dlg.setWindowTitle("Exit")
        dlg.setModal(True)
        dlg.setFixedSize(200, 150)
        dlg.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        dlg.setLayout(layout)

        label = QLabel("Do you really want to exit?")
        layout.addWidget(label)

        btn_yes = QPushButton("Yes")
        btn_yes.clicked.connect(dlg.accept)
        layout.addWidget(btn_yes)

        btn_no = QPushButton("No")
        btn_no.clicked.connect(dlg.close)
        layout.addWidget(btn_no)

        result = dlg.exec_()
        dlg.show()

        if result == QDialog.Accepted:
            print("Stopping Workers..")
            self.event_emitter.emit(EventType.E_GAME_STOP, 'kill_threads')
            print("Exiting..")
            sys.exit()

    def mousePressEvent(self, a0, QMouseEvent=None):
        print("Mouse pressed")
        print("-" * 80)
        print("button", a0.button())
        print("position", a0.pos())
        print("global position", a0.globalPos())


if __name__ == '__main__':
    event_emitter = EventEmitter()

    player1 = Player("Player", 0, event_emitter)
    player2 = Player("Opponent", 1, event_emitter)

    Game(event_emitter=event_emitter, player1=player1, player2=player2).run()

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    window = GLWindow(event_emitter, screen)

    event_emitter.start_workers()

    window.show()
    app.exec_()
