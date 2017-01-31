# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QMenuBar, QMenu, QAction, QMainWindow

from core.logger import get_logger
from core.evemon import get_evemon_instance

from .api_tester import ApitestMainWindow


class PYEVEMonMainWindow(QMainWindow):
    def __init__(self):
        super(PYEVEMonMainWindow, self).__init__(parent=None)
        self.logger = get_logger(__name__, logging.DEBUG)
        self.evemon = get_evemon_instance()
        self.logger.debug('Constructed window!')

        self.setMinimumSize(400, 300)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)

        self.menubar = self.menuBar()
        menu = QMenu(self.tr('Tools'), self.menubar)  # QMenu(self.tr('Tools'))
        action = menu.addAction('API Tester')
        action.triggered.connect(self.on_action_api_tester)

        self.menubar.addMenu(menu)

        # child windows
        self.apitmw = None

    @pyqtSlot(bool)
    def on_action_api_tester(self, checked: bool = False):
        # self.logger.debug('on_action_api_tester(): checked = {}'.format(checked))
        if self.apitmw is None:
            self.apitmw = ApitestMainWindow()
            self.apitmw.mainwindow = self
        self.apitmw.raise_()
