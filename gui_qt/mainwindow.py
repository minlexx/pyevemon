# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMenu, QAction, QMainWindow, QMessageBox, QTabWidget

from core.logger import get_logger
from core.em_core import get_core_instance, get_evelink_version_str

from version import get_pyevemon_version

from .api_tester import ApitestMainWindow
from .apikeys_manager import ApikeysManagerWindow
from .tabs import OverviewTab


class QtEmMainWindow(QMainWindow):
    def __init__(self):
        super(QtEmMainWindow, self).__init__(parent=None)
        self._logger = get_logger(__name__)
        self.evemon = get_core_instance()
        self._logger.debug('Constructed window!')

        self.setMinimumSize(640, 480)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)

        self.create_actions()
        self.create_menu()

        self.init_layout()
        self.create_tabs()

        # child popup windows
        self.apitmw = None
        self.apikeysmgrw = None

    def init_layout(self):
        # tab container
        self.tabwidget = QTabWidget(self)
        self.setCentralWidget(self.tabwidget)

    def create_actions(self):
        # QAction(const QString &text, QObject *parent = nullptr)
        self.action_manage_apikeys = QAction(self.tr('Manage API keys...'), self)
        self.action_manage_apikeys.triggered.connect(self.on_action_manage_apikeys)
        self.action_api_tester = QAction(self.tr('API Tester'), self)
        self.action_api_tester.triggered.connect(self.on_action_api_tester)
        self.action_about = QAction(self.tr('About...'), self)
        self.action_about.triggered.connect(self.on_action_about)
        self.action_about_qt = QAction(self.tr('About Qt...'), self)
        self.action_about_qt.triggered.connect(self.on_action_about_qt)

    def create_menu(self):
        # Construct menu; Api Keys
        self.menubar = self.menuBar()
        menu = QMenu(self.tr('API Keys'), self.menubar)
        menu.addAction(self.action_manage_apikeys)
        self.menubar.addMenu(menu)
        # Tools
        menu = QMenu(self.tr('Tools'), self.menubar)
        menu.addAction(self.action_api_tester)
        self.menubar.addMenu(menu)
        # Help
        menu = QMenu(self.tr('Help'), self.menubar)
        menu.addAction(self.action_about)
        menu.addAction(self.action_about_qt)
        self.menubar.addMenu(menu)

    def create_tabs(self):
        self.tabs = []
        tab = OverviewTab(self.tabwidget)
        self.tabs.append(tab)
        # int addTab(QWidget *page, const QString &label)
        tab_idx = self.tabwidget.addTab(tab, self.tr('Overview'))
        self._logger.debug('add overview tab at index = {}'.format(tab_idx))

    def recreate_tabs(self):
        # TODO: delete all tabs
        self.create_tabs()

    @pyqtSlot(bool)
    def on_action_api_tester(self, checked: bool = False):
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
        text += '\nUsing evelink library, version {}'.format(get_evelink_version_str())
        QMessageBox.about(self, title, text)

    @pyqtSlot(bool)
    def on_action_about_qt(self, checked: bool = False):
        QMessageBox.aboutQt(self)

    @pyqtSlot(bool)
    def on_action_manage_apikeys(self, checked: bool = False):
        if self.apikeysmgrw is None:
            self.apikeysmgrw = ApikeysManagerWindow()
            self.apikeysmgrw.mainwindow = self
        self.apikeysmgrw.raise_()
