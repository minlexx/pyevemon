# -*- coding: utf-8 -*-
import logging

from PyQt5.QtGui import QFont, QIcon, QCloseEvent
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, \
    QPushButton, QLayout, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QMessageBox

from core.logger import get_logger
from core.em_core import get_core_instance
from core.models import EmApiKey


class SingleApiKeyWidget(QWidget):

    editClicked = pyqtSignal('QString')
    removeClicked = pyqtSignal('QString')

    def __init__(self, parent):
        super(SingleApiKeyWidget, self).__init__(parent)
        self._logger = get_logger(__name__, logging.DEBUG)
        #
        self._layout = QHBoxLayout()
        self._layout.setSpacing(0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        #
        self._lbl_keyname = QLabel('', self)
        font = self._lbl_keyname.font()
        font.setWeight(QFont.Bold)
        self._lbl_keyname.setFont(font)
        self._lbl_keyname.setMinimumSize(100, 25)
        self._lbl_keyname.setMaximumHeight(25)
        self._lbl_keyid = QLabel('', self)
        self._lbl_keyid.setMinimumSize(100, 25)
        self._lbl_keyid.setMaximumHeight(25)
        self._lbl_keyid.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse |
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse)
        self._lbl_vcode = QLabel('', self)
        self._lbl_vcode.setMinimumSize(450, 25)
        self._lbl_vcode.setMaximumHeight(25)
        self._lbl_vcode.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse |
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse)
        self._layout_v = QVBoxLayout()
        self._layout_v.addWidget(self._lbl_keyname)
        self._layout_v.addWidget(self._lbl_keyid)
        self._layout_v.addWidget(self._lbl_vcode)
        self._layout_v.setSizeConstraint(QLayout.SetMinimumSize)
        self._layout.addLayout(self._layout_v)
        self._btn_edit = QPushButton(self.tr('Edit...'), self)
        self._btn_edit.setMinimumHeight(25)
        self._btn_edit.clicked.connect(self.on_btn_clicked_edit)
        self._btn_remove = QPushButton(self.tr('Remove'), self)
        self._btn_remove.setMinimumHeight(25)
        self._btn_remove.clicked.connect(self.on_btn_clicked_remove)
        self._layout.addStretch()
        self._layout.addWidget(self._btn_edit)
        self._layout.addWidget(self._btn_remove)
        self._layout.setSizeConstraint(QLayout.SetMinimumSize)
        #
        self.show()
        #
        self._apikey = None

    def set_from_apikey(self, apikey: EmApiKey):
        self._apikey = apikey
        self._lbl_keyname.setText(self.tr('Name') + ': ' + apikey.friendly_name)
        self._lbl_keyid.setText('keyId: ' + apikey.keyid)
        self._lbl_vcode.setText('vCode: ' + apikey.vcode)

    def on_btn_clicked_edit(self, checked: bool = False):
        self._logger.debug('emit editClicked({})'.format(self._apikey.keyid))
        self.editClicked.emit(self._apikey.keyid)

    def on_btn_clicked_remove(self, checked: bool = False):
        self._logger.debug('emit removeClicked({})'.format(self._apikey.keyid))
        self.removeClicked.emit(self._apikey.keyid)


class ApikeysManagerWindow(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ApikeysManagerWindow, self).__init__(parent=parent)
        self._logger = get_logger(__name__, logging.DEBUG)
        self._logger.debug('Constructed window!')
        self.mainwindow = None
        self.emcore = get_core_instance()
        self.api_keys = []

        self.setMinimumSize(300, 100)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.tr('API Keys Manager'))

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        # labels
        self._lbl_apikeys = QLabel(self.tr('API keys:'), self)

        # buttons
        self._btn_add_apikey = QPushButton(self.tr('Add API key...'), self)
        self._btn_add_apikey.clicked.connect(self.on_click_add_apikey)

        # layouts
        self._layout_top1 = QHBoxLayout()
        self._layout_top1.addWidget(self._lbl_apikeys)
        self._layout_top1.addStretch()
        self._layout_top1.addWidget(self._btn_add_apikey)

        self._layout.addLayout(self._layout_top1, 0)
        self._layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.load_keys()
        self.show()

    # void QWidget::closeEvent(QCloseEvent * event)
    def closeEvent(self, close_event: QCloseEvent):
        self._logger.debug('ApikeysManagerWindow.closeEvent()')
        self.mainwindow.apikeysmgrw = None
        close_event.accept()

    def load_keys(self):
        apikeys = self.emcore.savedata.get_apikeys()
        for apikey in apikeys:
            apikey_widget = SingleApiKeyWidget(self)
            apikey_widget.set_from_apikey(apikey)
            apikey_widget.editClicked.connect(self.on_click_edit_apikey)
            apikey_widget.removeClicked.connect(self.on_click_remove_apikey)
            self._layout.addWidget(apikey_widget, 0)
        #
        self._layout.addStretch()

    def on_click_edit_apikey(self, keyid: str):
        self._logger.debug('keyid = {}'.format(keyid))

    def on_click_add_apikey(self):
        self._logger.debug('click')

    def on_click_remove_apikey(self, keyid: str):
        self._logger.debug('keyid = {}'.format(keyid))