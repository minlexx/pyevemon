# -*- coding: utf-8 -*-
import logging
import sys

import sip

from PyQt5.QtCore import PYQT_VERSION_STR
from PyQt5.QtWidgets import QApplication

import version
import core.logger
import gui_qt.mainwindow


def start_gui():
    logger = core.logger.get_logger(__name__, logging.DEBUG)
    logger.info('Qt gui starting, PyQt5 version: {}; sip version: {}'.format(
        PYQT_VERSION_STR, sip.SIP_VERSION_STR))

    sip.setdestroyonexit(False)
    ver = version.get_pyevemon_version()

    app = QApplication(sys.argv)
    app.setApplicationVersion(ver['version'])
    app.setApplicationName(ver['app_name'])
    app.setApplicationDisplayName(ver['app_displayname'])
    app.setOrganizationDomain(ver['app_domain'])
    app.setOrganizationName(ver['author_name'])

    # print(app.applicationName(), app.applicationDirPath(), app.applicationPid())
    # print(app.applicationDisplayName(), app.applicationVersion())

    mainwindow = gui_qt.mainwindow.PYEVEMonMainWindow()
    mainwindow.show()

    return app.exec_()
