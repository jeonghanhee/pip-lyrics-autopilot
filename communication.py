# communication.py
from PyQt5.QtCore import pyqtSignal, QObject

class Communication(QObject):
    update_signal = pyqtSignal(str)