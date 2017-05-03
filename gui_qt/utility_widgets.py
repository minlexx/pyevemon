# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class LabelWithOkCancelIcon(QWidget):
    """
    Displays small icon with ok/cancel icon and a text to the right.
    """
    def __init__(self, parent: QWidget = None):
        super(LabelWithOkCancelIcon, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.icon_label = QLabel(self)
        self.label = QLabel(self)
        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.label)
        self.layout.addStretch()
        self.pixmap = QPixmap()
        self._ok_status = False

    def setIconAndText(self, ok_status: bool, text: str):
        self.label.setText(text)
        self._ok_status = ok_status
        if ok_status:
            self.pixmap.load('img/ok_icon.png')
        else:
            self.pixmap.load('img/cancel_icon.png')
        self.icon_label.setPixmap(self.pixmap.scaled(32, 32))

    def text(self) -> str:
        return str(self.label.text())

    def ok_status(self) -> bool:
        return self._ok_status
