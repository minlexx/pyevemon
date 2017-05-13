# -*- coding: utf-8 -*-
import datetime
import logging

from PyQt5.QtGui import QFont, QIcon, QCloseEvent
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QDialog, QLineEdit,  QPushButton, \
    QLayout, QLayoutItem, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox, \
    QWizard, QWizardPage

from core.logger import get_logger
from core.em_core import get_core_instance, EmCore
from core.models import EmApiKey, EveApiAccessMask

from .utility_widgets import LabelWithOkCancelIcon


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
        if self._apikey.friendly_name is None:
            self._apikey.friendly_name = ''
        self._lbl_keyname.setText(self.tr('Name') + ': ' + apikey.friendly_name)
        self._lbl_keyid.setText('keyId: ' + apikey.keyid)
        self._lbl_vcode.setText('vCode: ' + apikey.vcode)

    def on_btn_clicked_edit(self, checked: bool = False):
        self._logger.debug('emit editClicked({})'.format(self._apikey.keyid))
        self.editClicked.emit(self._apikey.keyid)

    def on_btn_clicked_remove(self, checked: bool = False):
        self._logger.debug('emit removeClicked({})'.format(self._apikey.keyid))
        self.removeClicked.emit(self._apikey.keyid)


class AddEditApikeyDialog(QWizard):
    def __init__(self, parent: QWidget, apikey: EmApiKey = None):
        super(AddEditApikeyDialog, self).__init__(parent)

        self._logger = get_logger(__name__, logging.DEBUG)
        self._apikey = EmApiKey()
        if apikey is not None:
            self._apikey.keyid = apikey.keyid
            self._apikey.vcode = apikey.vcode
            self._apikey.friendly_name = ''
            if apikey.friendly_name is not None:
                self._apikey.friendly_name = apikey.friendly_name

        self.setSizeGripEnabled(True)
        self.setMinimumSize(300, 200)
        self.icon = QIcon('img/pyevemon.png')
        self.setWindowIcon(self.icon)

        if not self._apikey.is_empty():
            self.setWindowTitle(self.tr('Edit API key'))
        else:
            self.setWindowTitle(self.tr('Add API key'))

        # wizard pages.
        # Page 1: API key ID / vcode input
        self.page1 = QWizardPage(self)
        self.page1.setTitle(self.tr('API Key ID / vCode input'))
        self.page1.setSubTitle(self.tr('Edit API key ID and vCode'))
        self.page1.l = QGridLayout()
        self.page1.setLayout(self.page1.l)
        self.page1.lbl_keyID = QLabel(self.tr('API key ID:'), self.page1)
        self.page1.lbl_vcode = QLabel(self.tr('API key vCode:'), self.page1)
        self.page1.le_keyID = QLineEdit(self.page1)
        self.page1.le_vcode = QLineEdit(self.page1)
        self.page1.lbl_keyID.setBuddy(self.page1.le_keyID)
        self.page1.lbl_vcode.setBuddy(self.page1.le_vcode)
        self.page1.l.addWidget(self.page1.lbl_keyID, 0, 0)
        self.page1.l.addWidget(self.page1.le_keyID, 0, 1)
        self.page1.l.addWidget(self.page1.lbl_vcode, 1, 0)
        self.page1.l.addWidget(self.page1.le_vcode, 1, 1)
        self.page1.registerField('keyid', self.page1.le_keyID)
        self.page1.registerField('vcode', self.page1.le_vcode)

        self.page2 = QWizardPage(self)
        self.page2.setTitle(self.tr('API Key type and access mask'))
        # self.page2.setSubTitle(self.tr('Check thar API key has acceptable access rights'))
        self.page2.l = QVBoxLayout()
        self.page2.l1 = QHBoxLayout()  # key type
        self.page2.l2 = QHBoxLayout()  # access mask
        self.page2.l3 = QHBoxLayout()  # characters
        self.page2.l4 = QHBoxLayout()  # expires
        self.page2.lx = QGridLayout()  # checks grid
        self.page2.setLayout(self.page2.l)
        self.page2.l.addLayout(self.page2.l1)
        self.page2.l.addLayout(self.page2.l2)
        self.page2.l.addLayout(self.page2.l3)
        self.page2.l.addLayout(self.page2.l4)
        self.page2.l.addLayout(self.page2.lx)
        #
        self.page2.lbl_keytype = QLabel(self.tr('API Key type:'), self.page2)
        self.page2.lbl_keytype_v = QLabel('', self.page2)
        self.page2.lbl_accessmask = QLabel(self.tr('API Key access mask:'), self.page2)
        self.page2.lbl_accessmask_v = QLabel('', self.page2)
        self.page2.lbl_characters = QLabel(self.tr('Characters:'), self.page2)
        self.page2.lbl_characters_v = QLabel('', self.page2)
        self.page2.lbl_expires = QLabel(self.tr('Expires:'), self.page2)
        self.page2.lbl_expires_v = QLabel('', self.page2)
        self.page2.l1.addWidget(self.page2.lbl_keytype)
        self.page2.l1.addWidget(self.page2.lbl_keytype_v)
        self.page2.l1.addStretch()
        self.page2.l2.addWidget(self.page2.lbl_accessmask)
        self.page2.l2.addWidget(self.page2.lbl_accessmask_v)
        self.page2.l2.addStretch()
        self.page2.l3.addWidget(self.page2.lbl_characters)
        self.page2.l3.addWidget(self.page2.lbl_characters_v)
        self.page2.l3.addStretch()
        self.page2.l4.addWidget(self.page2.lbl_expires)
        self.page2.l4.addWidget(self.page2.lbl_expires_v)
        self.page2.l4.addStretch()
        #
        self.page2.w_basicfuncs = LabelWithOkCancelIcon(self.page2)
        self.page2.w_basicfuncs.set_text(self.tr('Basic character info'))
        self.page2.lx.addWidget(self.page2.w_basicfuncs, 0, 0)
        self.page2.w_skills = LabelWithOkCancelIcon(self.page2)
        self.page2.w_skills.set_text(self.tr('Skills monitoring'))
        self.page2.lx.addWidget(self.page2.w_skills, 1, 0)
        #
        self.page3 = QWizardPage(self)
        self.page3.l = QVBoxLayout()
        self.page3.setLayout(self.page3.l)
        self.page3.lbl_keyname = QLabel(self.tr('Enter key name:'), self.page3)
        self.page3.le_keyname = QLineEdit(self)
        self.page3.l.addWidget(self.page3.lbl_keyname)
        self.page3.l.addWidget(self.page3.le_keyname)
        self.page3.registerField('keyname', self.page3.le_keyname)

        self.addPage(self.page1)
        self.addPage(self.page2)
        self.addPage(self.page3)

        # wizard options
        self.setOption(QWizard.HaveHelpButton, False)

    def get_apikey(self) -> EmApiKey:
        return self._apikey

    def show_popup_warning(self, m: str):
        self._logger.warning(m)
        QMessageBox.warning(self, self.tr('Warning'), m)

    def initializePage(self, page_id):
        """ This virtual function is called by QWizard to prepare page id just before it is shown """
        self._logger.debug('page_id = {}'.format(page_id))
        if page_id == 0:
            self.page1.le_keyID.setText(self._apikey.keyid)
            self.page1.le_vcode.setText(self._apikey.vcode)
        elif page_id == 1:
            self.page2.lbl_keytype_v.setText(self._apikey.key_type)
            self.page2.lbl_accessmask_v.setText(str(self._apikey.access_mask))
            if self._apikey.expire_ts is None:
                self.page2.lbl_expires_v.setText(self.tr('Never'))
            else:
                s = str(self._apikey.expire_ts)
                if self._apikey.expired: s += '; ' + self.tr('Expired')
                self.page2.lbl_expires_v.setText(s)
            if self._apikey.key_type in [EmCore.KEY_TYPE_ACCOUNT, EmCore.KEY_TYPE_CHARACTER]:
                # fill characters
                self.page2.lbl_characters_v.setText(self._construct_apikeys_characters_str())
            # fill checks grid
            self.page2.w_basicfuncs.set_ok_status(self._check_key_good_basic_info())
            self.page2.w_skills.set_ok_status(self._check_key_good_skills())
        elif page_id == 2:
            keyname = self._construct_apikeys_characters_str()
            if self._apikey.friendly_name is not None:
                if self._apikey.friendly_name != '':
                    keyname = self._apikey.friendly_name
            self.page3.le_keyname.setText(keyname)

    def validateCurrentPage(self) -> bool:
        """ This virtual function is called by QWizard when the user clicks Next or Finish
        to perform some last-minute validation. If it returns true, the next page is shown
        (or the wizard finishes); otherwise, the current page stays up. """
        page_id = int(self.currentId())
        self._logger.debug('current Id = {}'.format(page_id))
        #
        if page_id == 0:
            # validate API key, get API key info
            self._apikey.keyid = self.field('keyid')
            self._apikey.vcode = self.field('vcode')
            self._logger.debug('Input fields: {} / {}'.format(self._apikey.keyid, self._apikey.vcode))
            if not self._apikey.is_valid():
                self.show_popup_warning(self.tr('Invalid input!'))
                return False
            # get apikey info from EVE API
            emcore = get_core_instance()
            emcore.set_apikey(self._apikey)
            keyinfo = emcore.api_call('account/APIKeyInfo')
            # {'type': 'account', 'characters': {91205062: {'alliance': {'id': 0, 'name': ''},
            #    'id': 91205062, 'name': 'Lexx Min', 'corp': {'id': 98369889, 'name': 'New Home Inc.'}},
            #    93013943: {'alliance': {'id': 0, 'name': ''}, 'id': 93013943, 'name': 'Alexxia Kion',
            #    'corp': {'id': 1000045, 'name': 'Science and Trade Institute'}}}, 'access_mask': 1073741823,
            #    'expire_ts': None}
            if keyinfo is not None:
                if type(keyinfo) == dict:
                    self._apikey.key_type = str(keyinfo['type'])
                    self._apikey.characters = keyinfo['characters']
                    self._apikey.access_mask = int(keyinfo['access_mask'])
                    self._apikey.expire_ts = keyinfo['expire_ts']
                    self._apikey.expired = False
                    cur_ts = datetime.datetime.utcnow().timestamp()
                    if self._apikey.expire_ts is not None:
                        if cur_ts > self._apikey.expire_ts:
                            self._apikey.expired = True
                    if self._apikey.expired:
                        self.show_popup_warning(self.tr('Key has expired!'))
                        return False
                    return True
            else:
                le = emcore.get_last_error()
                warnmsg = self.tr('EVE api call account/APIKeyInfo failed!')
                if le is not None:
                    warnmsg += '\n' + self.tr('Error message was:') + ' ' + le[1]
                self.show_popup_warning(warnmsg)
                return False
        elif page_id == 1:
            if self._apikey.key_type == EmCore.KEY_TYPE_CORPORATION:
                self.show_popup_warning(self.tr('Cannot monitor corporation API keys.'))
                return False
            if not self._check_key_good_basic_info():
                self.show_popup_warning(self.tr('This key has too restricted access mask, \n'
                                                'it cannot be used even for basic information.'))
                return False
        elif page_id == 2:
            keyname = self.field('keyname')
            if keyname == '':
                self.show_popup_warning(self.tr('Key friendly name should not be empty!'))
                return False
            self._apikey.friendly_name = keyname
        return True

    def _construct_apikeys_characters_str(self) -> str:
        s = ''
        for charid in self._apikey.characters.keys():
            if s != '': s += ', '
            s += self._apikey.characters[charid]['name']
        return s

    def _key_has_mask(self, bitmask: int) -> bool:
        return (self._apikey.access_mask & bitmask) > 0

    def _check_key_good_basic_info(self):
        has_charsheet = self._key_has_mask(EveApiAccessMask.CharacterSheet)
        has_charinfo = self._key_has_mask(EveApiAccessMask.CharacterInfo_public) \
                       or self._key_has_mask(EveApiAccessMask.CharacterInfo_private)
        self._logger.debug('has_charsheet={}, has_charinfo={}'.format(has_charsheet, has_charinfo))
        return has_charsheet and has_charinfo

    def _check_key_good_skills(self):
        has_skills = self._key_has_mask(EveApiAccessMask.CharacterSheet) \
                     or self._key_has_mask(EveApiAccessMask.Skills)
        has_skillintraining = self._key_has_mask(EveApiAccessMask.SkillInTraining)
        has_skillqueue = self._key_has_mask(EveApiAccessMask.SkillQueue)
        self._logger.debug('has_skills={}, has_skillqueue={}, has_skillintraining={}'.format(
            has_skills, has_skillqueue, has_skillintraining))
        return has_skills and has_skillqueue and has_skillintraining


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

        self.load_apikeys()
        self.show()

    # void QWidget::closeEvent(QCloseEvent * event)
    def closeEvent(self, close_event: QCloseEvent):
        self._logger.debug('ApikeysManagerWindow.closeEvent()')
        self.mainwindow.apikeysmgrw = None
        close_event.accept()

    def load_apikeys(self):
        apikeys = self.emcore.savedata.get_apikeys()
        for apikey in apikeys:
            apikey_widget = SingleApiKeyWidget(self)
            apikey_widget.set_from_apikey(apikey)
            apikey_widget.editClicked.connect(self.on_click_edit_apikey)
            apikey_widget.removeClicked.connect(self.on_click_remove_apikey)
            self._layout.addWidget(apikey_widget, 0)
        #
        self._layout.addStretch()

    def reload_apikeys(self):
        # clear existing layout
        lc = self._layout.count()
        i = lc - 1  # iterate from the end
        # at index 0 there is a layout_top1
        # we need items from index 1 and to the end
        while i > 0:
            layoutItem = self._layout.itemAt(i)
            if layoutItem is not None:
                can_del = False
                # we can delete only spacers and sub-widgets; skip layouts
                if layoutItem.spacerItem() is not None:
                    can_del = True
                if layoutItem.widget() is not None:
                    can_del = True
                if can_del:
                    self._layout.removeItem(layoutItem)
                    del layoutItem
            i -= 1
        self.load_apikeys()

    def start_add_or_edit_apikey(self, keyid: str = None):
        apikey = None
        if keyid is not None:
            apikey = self.emcore.savedata.get_apikey_by_keyid(keyid)
        dlg = AddEditApikeyDialog(self, apikey)
        exec_res = dlg.exec_()
        if exec_res == QDialog.Rejected: return
        # apply added/edited apikey
        self.emcore.savedata.store_apikey(dlg.get_apikey(), check_existing=False)
        self.reload_apikeys()

    def on_click_add_apikey(self):
        self._logger.debug('click')
        self.start_add_or_edit_apikey()

    def on_click_edit_apikey(self, keyid: str):
        self._logger.debug('keyid = {}'.format(keyid))
        self.start_add_or_edit_apikey(keyid)

    def on_click_remove_apikey(self, keyid: str):
        self._logger.debug('keyid = {}'.format(keyid))
        self.emcore.savedata.remove_apikey_by_keyid(keyid)
        self.reload_apikeys()
