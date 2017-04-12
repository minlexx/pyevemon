# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QGuiApplication, QIcon, QCloseEvent
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, \
    QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QMessageBox

from core.logger import get_logger
from core.em_core import get_core_instance
from core.models import EmApiKey


class ApikeysManagerWindow(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ApikeysManagerWindow, self).__init__(parent=parent)
        self._logger = get_logger(__name__, logging.DEBUG)
        self._logger.debug('Constructed window!')
        self.mainwindow = None
        self.emcore = get_core_instance()
        self.api_keys = []

        self.setMinimumSize(640, 480)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.tr('API Keys Manager'))

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        # labels
        #self._lbl_api_method = QLabel('API call:', self)

        # combos
        #self._cmb_apicall = QComboBox(self)

        # edits
        #self._edit_keyid = QLineEdit(self)

        # buttons
        #self._btn_exec_call = QPushButton('Execute call', self)
        #self._btn_exec_call.clicked.connect(self.on_click_execute_call)

        # layouts
        #self._layout_top1 = QHBoxLayout()
        #self._layout_top1.addWidget(self._lbl_api_method)
        #self._layout_top1.addStretch()

        #self._layout.addLayout(self._layout_top1, 0)

        self.show()

    # void QMainWindow::closeEvent(QCloseEvent * event)
    def closeEvent(self, close_event: QCloseEvent):
        self._logger.debug('ApikeysManagerWindow.closeEvent()')
        self.mainwindow.apikeysmgrw = None
        close_event.accept()
