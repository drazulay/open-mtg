import array
import random
import sys

import numpy as np
import PIL.Image as Image

from events import EventEmitter, EventType
from game import Game, Player, EventLoop

from OpenGL.GL import *
import OpenGL.arrays.vbo as glvbo

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import QGLWidget


class GLWidget(QGLWidget):
    def __init__(self, data: list = None, parent=None):
        super().__init__(parent)
        self.data = None
        if data is None:
            data = np.array([])
        self.set_data(data)
        self.count = None
        self.vbo = None
        self.width = 1024
        self.height = 600

        self.setGeometry(0, 0, self.width, self.height)
        self.setBaseSize(self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setContentsMargins(0, 0, 0, 0)

    def initializeGL(self):
        print("Initializing OpenGL")
        glClearColor(0, 0, 0, 0)
        self.vbo = glvbo.VBO(self.data)
        self.vbo.bind()

    def resizeGL(self, w, h):
        self.width, self.height = w, h

        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1, 1, 1, -1, -1, 1)

    def paintGL(self):
        print("Drawing Pre-Match Screen")
        glColor(1, 1, 0)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, self.vbo)
        glDrawArrays(GL_POINTS, 0, len(self.data))

        text_id = self.load_texture("data/images/btn_duel.png")
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_quad(0, 0, text_id)

    def load_texture(self, texture):
        try:
            text = Image.open(texture)
        except IOError as ex:
            print("Failed to open texture file: ", texture)
            text = Image.open("data/images/btn_duel.png")

        text_data = np.array(list(text.getdata()))
        text_id = glGenTextures(1)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, text_id)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text.size[0], text.size[1], 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        text.close()

        return text_id

    def draw_quad(self, centerX, centerY, textureID):
        verts = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        texts = ((1, 0), (1, 1), (0, 1), (0, 0))
        surf = (0, 1, 2, 3)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)

        glBegin(GL_QUADS)
        for i in surf:
            glTexCoord2f(texts[i][0], texts[i][1])
            glVertex2f(centerX + verts[i][0], centerY + verts[i][1])
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def set_data(self, data):
        """Load 2D data as a Nx2 Numpy array.
        """
        self.data = data
        self.count = data.shape[0]

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

        # initialize the GL widget
        self.data = np.array(.2 * np.random.randn(100000, 2), dtype=np.float32)
        self.glWidget = GLWidget(self.data)

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
