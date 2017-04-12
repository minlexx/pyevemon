# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QMenuBar, QMenu, QAction, QMainWindow, QMessageBox

from core.logger import get_logger
from core.em_core import get_core_instance

from version import get_pyevemon_version

from .api_tester import ApitestMainWindow


class QtEmMainWindow(QMainWindow):
    def __init__(self):
        super(QtEmMainWindow, self).__init__(parent=None)
        self._logger = get_logger(__name__, logging.DEBUG)
        self.evemon = get_core_instance()
        self._logger.debug('Constructed window!')

        self.setMinimumSize(400, 300)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)

        # Construct menu
        self.menubar = self.menuBar()
        menu = QMenu(self.tr('API Keys'), self.menubar)
        action = menu.addAction(self.tr('Manage API keys...'))
        action.triggered.connect(self.on_action_manage_apikeys)
        self.menubar.addMenu(menu)

        menu = QMenu(self.tr('Tools'), self.menubar)
        action = menu.addAction(self.tr('API Tester'))
        action.triggered.connect(self.on_action_api_tester)
        self.menubar.addMenu(menu)

        menu = QMenu(self.tr('Help'), self.menubar)
        action = menu.addAction(self.tr('About...'))
        action.triggered.connect(self.on_action_about)
        action = menu.addAction(self.tr('About Qt...'))
        action.triggered.connect(self.on_action_about_qt)
        self.menubar.addMenu(menu)

        # child windows
        self.apitmw = None

    @pyqtSlot(bool)
    def on_action_api_tester(self, checked: bool = False):
        # self._logger.debug('on_action_api_tester(): checked = {}'.format(checked))
        if self.apitmw is None:
            self.apitmw = ApitestMainWindow()
            self.apitmw.mainwindow = self
        self.apitmw.raise_()

    @pyqtSlot(bool)
    def on_action_about(self, checked: bool = False):
        v = get_pyevemon_version()
        title = self.tr('About') + ' ' + v['app_name']
        text = v['version_str'] + '\n'
        text += '\n' + self.tr('Website') + ': ' + v['website_url']
        text += '\n' + self.tr('Author') + ': ' + v['author_name'] + ' (' + v['author_email'] + ')'
        QMessageBox.about(self, title, text)

    @pyqtSlot(bool)
    def on_action_about_qt(self, checked: bool = False):
        QMessageBox.aboutQt(self)

    @pyqtSlot(bool)
    def on_action_manage_apikeys(self, checked: bool = False):
        pass
