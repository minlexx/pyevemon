# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget


class AbstractBaseTab(QWidget):

    TAB_TYPE_NONE = ''
    TAB_TYPE_OVERVIEW = 'over'
    TAB_TYPE_CHARACTER = 'char'

    def __init__(self, parent: QWidget = None):
        super(AbstractBaseTab, self).__init__(parent)
        # override in child classes
        self._tab_type = AbstractBaseTab.TAB_TYPE_NONE

    def tab_type(self) -> str:
        return self._tab_type
