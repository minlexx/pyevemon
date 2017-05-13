# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel


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


class OverviewTab(AbstractBaseTab):
    def __init__(self, parent: QWidget = None):
        super(OverviewTab, self).__init__(parent)
        self._tab_type = AbstractBaseTab.TAB_TYPE_OVERVIEW
        self._layout = QGridLayout()
        self._layout.setContentsMargins(2, 2, 2, 2)
        self._layout.setSpacing(3)
        self.setLayout(self._layout)
        #
        self.lbl = QLabel('Overview tab', self)
        self._layout.addWidget(self.lbl, 0, 0)
