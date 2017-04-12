# -*- coding: utf-8 -*-
import json
import logging

from PyQt5.QtGui import QIcon, QCloseEvent
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, \
    QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QMessageBox

from core.logger import get_logger
from core.em_core import get_core_instance
from core.models import EmApiKey


class ApitestMainWindow(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ApitestMainWindow, self).__init__(parent=parent)
        self._logger = get_logger(__name__, logging.DEBUG)
        self._logger.debug('Constructed window!')
        self.mainwindow = None
        self.emcore = get_core_instance()
        self.api_keys = []

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
        self._lbl_api_key = QLabel('Select API key:', self)
        self._lbl_charid = QLabel('Char ID:', self)

        # combos
        self._cmb_apicall = QComboBox(self)
        self._cmb_apicall.setMinimumWidth(200)
        self._cmb_apikey = QComboBox(self)
        self._cmb_apikey.setMinimumWidth(150)
        self._cmb_apikey.currentIndexChanged.connect(self.on_change_selected_apikey)

        # edits
        self._edit_keyid = QLineEdit(self)
        self._edit_keyid.setMaximumWidth(100)
        self._edit_vcode = QLineEdit(self)
        self._edit_result = QPlainTextEdit(self)
        self._edit_result.setReadOnly(True)
        self._edit_charid = QLineEdit(self)
        self._edit_charid.setMaximumWidth(100)

        # buttons
        self._btn_exec_call = QPushButton('Execute call', self)
        self._btn_exec_call.clicked.connect(self.on_click_execute_call)
        self._btn_exec_call.setDefault(True)
        self._btn_add_new_apikey = QPushButton('Add new key', self)
        self._btn_add_new_apikey.clicked.connect(self.on_click_add_new_apikey)

        # layouts
        self._layout_top1 = QHBoxLayout()
        self._layout_top1.addWidget(self._lbl_api_method)
        self._layout_top1.addWidget(self._cmb_apicall)
        self._layout_top1.addWidget(self._lbl_api_key)
        self._layout_top1.addWidget(self._cmb_apikey)
        self._layout_top1.addStretch()
        self._layout_top1.addWidget(self._btn_exec_call)

        self._layout_top2 = QHBoxLayout()
        self._layout_top2.addWidget(self._lbl_keyid)
        self._layout_top2.addWidget(self._edit_keyid)
        self._layout_top2.addWidget(self._lbl_vcode)
        self._layout_top2.addWidget(self._edit_vcode)
        self._layout_top2.addWidget(self._btn_add_new_apikey)

        self._layout_top3 = QHBoxLayout()
        self._layout_top3.addWidget(self._lbl_charid)
        self._layout_top3.addWidget(self._edit_charid)
        self._layout_top3.addStretch()

        self._layout_bot = QHBoxLayout()
        self._layout_bot.addWidget(self._edit_result)

        self._layout.addLayout(self._layout_top1, 0)
        self._layout.addLayout(self._layout_top2, 0)
        self._layout.addLayout(self._layout_top3, 0)
        self._layout.addLayout(self._layout_bot, 1)

        self.fill_data()

        self.show()

    # void MainWindow::closeEvent(QCloseEvent * event)
    def closeEvent(self, close_event: QCloseEvent):
        self._logger.debug('ApitestMainWindow.closeEvent()')
        self.mainwindow.apitmw = None
        close_event.accept()

    def fill_apikeys(self):
        self._cmb_apikey.clear()
        self.api_keys = self.emcore.savedata.get_apikeys()
        for api_key in self.api_keys:
            s = api_key.keyid
            if api_key.friendly_name is not None:
                s = '{} ({})'.format(api_key.friendly_name, api_key.keyid)
            self._cmb_apikey.addItem(s, api_key.keyid)

    def fill_data(self):
        # API calls
        self._cmb_apicall.clear()
        supported_apicalls = sorted(self.emcore.get_supported_apicalls())
        for apicall in supported_apicalls:
            self._cmb_apicall.addItem(apicall)
        # API keys
        self.fill_apikeys()

    # result can be dict or list
    def fill_result(self, result):
        if result is not None:
            if (type(result) == dict) or (type(result) == list):
                self._edit_result.clear()
                as_json = json.dumps(result, indent=4)
                self._edit_result.setPlainText(as_json)
                #
                # autofill char_id from certain replies
                apicall = self._cmb_apicall.currentText()
                charids = []
                if apicall == 'account/APIKeyInfo':
                    charids = list(result['characters'])
                if apicall == 'account/Characters':
                    charids = list(result)
                if len(charids) > 0:
                    if self._edit_charid.text() == '':
                        self._edit_charid.setText(str(charids[0]))
            else:
                self._logger.warning('Unhandled result type: {}'.format(type(result)))

    @pyqtSlot(bool)
    def on_click_execute_call(self, checked: bool):
        # self._logger.debug('on_click_execute_call')
        apicall = self._cmb_apicall.currentText()
        # self._logger.debug('Api call: {}'.format(apicall))

        keyid = self._edit_keyid.text()
        vcode = self._edit_vcode.text()
        if (keyid == '') or (vcode == ''):
            QMessageBox.warning(self, 'Please fill in data!',
                                'Cannot send request with empty API keyd/vcode')
            return

        kwargs = {}

        if apicall.startswith('char/'):
            charid = None
            try:
                charid = int(self._edit_charid.text())
            except ValueError:
                pass
            kwargs['char_id'] = charid

        current_apikey = EmApiKey(keyid, vcode)
        self.emcore.set_apikey(current_apikey)
        # self._logger.debug('Set current apikey: {}'.format(current_apikey))

        result = self.emcore.api_call(apicall, **kwargs)
        if result is not None:
            self.fill_result(result)

    @pyqtSlot(bool)
    def on_click_add_new_apikey(self, checked: bool):
        # self._logger.debug('on_click_add_new_apikey')
        keyid = self._edit_keyid.text()
        vcode = self._edit_vcode.text()
        if (keyid == '') or (vcode == ''):
            self._logger.debug('keyid or vcode empty!')
            return
        apikey = EmApiKey(keyid, vcode)
        if apikey.is_valid():
            self.emcore.savedata.store_apikey(apikey)
            # reload existing api keys
            self.fill_apikeys()
        else:
            self._logger.error('Invalid input data for apikey: {}'.format(apikey))

    @pyqtSlot(int)
    def on_change_selected_apikey(self, idx: int):
        keyid = str(self._cmb_apikey.currentData())
        # self._logger.debug('idx: {}; keyid: {}'.format(idx, keyid))
        for apikey in self.api_keys:
            if apikey.keyid == keyid:
                self._edit_keyid.setText(keyid)
                self._edit_vcode.setText(apikey.vcode)
