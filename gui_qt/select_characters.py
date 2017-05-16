# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QGroupBox, \
    QCheckBox, QLabel

import core.logger
import core.em_core
from core.models import EmApiKey, EmApiKeyCharacter


class SelectCharactersDlg(QDialog):
    def __init__(self, parent: QWidget = None):
        super(SelectCharactersDlg, self).__init__(parent)

        self._logger = core.logger.get_logger(__name__)
        self.emcore = core.em_core.get_core_instance()

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self.setWindowTitle(self.tr('Select characters'))

        self.load_apikeys_and_characters()

    def load_apikeys_and_characters(self):
        apikeys = self.emcore.savedata.get_apikeys()
        if len(apikeys) == 0:
            lbl = QLabel(self.tr('No apikeys added! First add some EVE Api keys '
                                 '(Characters -> Manage API keys...).'), self)
            self._layout.addWidget(lbl)
            return
        for apikey in apikeys:
            gb = self.create_apikey_groupbox(apikey)
            self._layout.addWidget(gb)
        self._layout.addStretch()

    def create_apikey_groupbox(self, apikey: EmApiKey) -> QGroupBox:
        friendly_name = self.tr('Key') + ' ' + apikey.keyid
        if apikey.friendly_name is not None:
            friendly_name += ': ' + apikey.friendly_name
        gb = QGroupBox(friendly_name, self)
        layout = QVBoxLayout()
        gb.setLayout(layout)
        for char in apikey.apikey_characters:
            cb = QCheckBox(char.charname, gb)
            if char.is_selected is not None:
                if char.is_selected:
                    cb.setChecked(True)
            layout.addWidget(cb)
        return gb
