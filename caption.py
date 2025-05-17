from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
from threading import Thread
from utils import PATH, DEFAULT_FONT, FONT_SIZE, log
from window import get_pip_window
from random import randrange

class Caption(Thread):
    def __init__(self, communication):
        Thread.__init__(self)
        self.app = None
        self.communication = communication
        self.initUI()

    def initUI(self):
        self.app = QApplication.instance()
        self._window = QMainWindow()
        self._window.setWindowTitle("Caption")
        self._window.setWindowIcon(QIcon(PATH + "/images/icon.png"))

        self.caption = QLabel("")
        self.caption_font = QFont(DEFAULT_FONT, FONT_SIZE)

        self.caption.setAutoFillBackground(True)
        self.caption.setStyleSheet(
            """
            background-color: black;
            color: white;
            padding: 3px 5px 3px 5px;
            border-radius: 1px;
            """
        )
        self.caption.setFont(self.caption_font)
        self.caption.setAlignment(Qt.AlignCenter)

        self.timer = QTimer(self._window)
        self.timer.timeout.connect(self.update_window_position)
        self.timer.start(1)
        
        self._window.setWindowFlags(self._window.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self._window.setCentralWidget(self.caption)
        self._window.show()

        self.adjust_size()
        self.redenering()
        self.communication.update_signal.connect(self.set_caption_content)

    def set_caption_content(self, content):
        self.caption.setText(content)
        self.adjust_size()
        self.redenering()

    def adjust_size(self):
        w = self.caption.fontMetrics().width(self.caption.text()) + 15
        h = self.caption.fontMetrics().height()

        self._window.setFixedWidth(w)
        self._window.setFixedHeight(h)

        self.caption.setFixedWidth(w)
        self.caption.setFixedHeight(h)

    def update_window_position(self):
        try:
            pip_window_info = get_pip_window()
            left, top, right, bottom = pip_window_info
            
            self._window.move(
                ((left + right) // 2) - (self.caption.fontMetrics().width(self.caption.text()) // 2),
                bottom
            )
        except Exception as e:
            pass

    def redenering(self):
        if (len(self.caption.text()) <= 0):
            self._window.hide()
        else:
            self._window.show()