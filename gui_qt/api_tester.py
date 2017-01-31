# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QGuiApplication, QIcon, QCloseEvent
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, \
    QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit

from core.logger import get_logger
from core.evemon import get_evemon_instance


class ApitestMainWindow(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ApitestMainWindow, self).__init__(parent=parent)
        self.logger = get_logger(__name__, logging.DEBUG)
        self.logger.debug('Constructed window!')
        self.mainwindow = None

        self.setMinimumSize(640, 480)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('API Tester')

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        # labels
        self._lbl_api_method = QLabel('API call:', self)
        self._lbl_keyid = QLabel('keyID:', self)
        self._lbl_vcode = QLabel('vCode:', self)

        # combos
        self._cmb_api = QComboBox(self)
        self._cmb_api.setMinimumWidth(200)

        # edits
        self._edit_keyid = QLineEdit(self)
        self._edit_keyid.setMaximumWidth(100)
        self._edit_vcode = QLineEdit(self)
        self._edit_result = QPlainTextEdit(self)
        self._edit_result.setReadOnly(True)

        # layouts
        self._layout_top = QHBoxLayout()
        self._layout_top.addWidget(self._lbl_api_method)
        self._layout_top.addWidget(self._cmb_api)
        self._layout_top.addWidget(self._lbl_keyid)
        self._layout_top.addWidget(self._edit_keyid)
        self._layout_top.addWidget(self._lbl_vcode)
        self._layout_top.addWidget(self._edit_vcode)

        self._layout_bot = QHBoxLayout()
        self._layout_bot.addWidget(self._edit_result)

        self._layout.addLayout(self._layout_top, 0)
        self._layout.addLayout(self._layout_bot, 1)

        self.show()

    # void MainWindow::closeEvent(QCloseEvent * event)
    def closeEvent(self, close_event: QCloseEvent):
        self.logger.debug('ApitestMainWindow.closeEvent()')
        self.mainwindow.apitmw = None
        close_event.accept()
