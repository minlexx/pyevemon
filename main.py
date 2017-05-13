#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import logging
import os
import os.path
import sys

# Local imports
import version
import core.logger
import core.em_core


# def custom_unhandled_handler_func(bound_param, exc_type, exc_value, exc_traceback):
#    print(bound_param, exc_type, exc_value, exc_traceback)
#    # 123 <class 'ZeroDivisionError'> division by zero <traceback object at 0x02A8E030>


def main():
    ver = version.get_pyevemon_version()
    verstr = '{}; evelink version {}'.format(ver['version_str'], core.em_core.get_evelink_version_str())

    ap = argparse.ArgumentParser(prog=sys.argv[0], add_help=True,
                                 description='EVE Online character monitor using python, '
                                             'with a GUI frontend')
    ap.add_argument('--debug', action='store_true', help='Enable more debug output')
    ap.add_argument('--version', action='version', version=verstr)
    ap.add_argument('--gui', action='store', nargs='?', const='qt', default='qt', type=str,
                    choices=['qt'])
    args = ap.parse_args()

    # setup main logger only after arguments were parsed.
    # setup logging level before any logger is created
    core.logger.set_loglevel(logging.INFO)
    if args.debug:
        core.logger.set_loglevel(logging.DEBUG)
    core.logger.init_unhandled_exception_handling('unhandled_exceptions.log')
    # core.logger.add_unhandled_exception_handler(custom_unhandled_handler_func, 123)

    # my local logger object
    logger = core.logger.get_logger(__name__)

    is_64bit = '64 bit' in sys.version
    logger.info('{} version {}. Using python-{}.{}.{} {}, evelink-{}'.format(
        ver['app_displayname'], ver['version'],
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro,
        ('(64 bit)' if is_64bit else '(32 bit)'),
        core.em_core.get_evelink_version_str()
    ))

    frozen = getattr(sys, 'frozen', False)
    if frozen:
        script = sys.executable
        logger.debug('Frozen! Running as embedded python DLL, {}'.format(script))
    else:
        script = os.path.abspath(__file__)
        logger.debug('Not Frozen, running under pure python, {}'.format(script))

    # set current directory to script executable path
    scriptdir = os.path.dirname(script)
    logger.debug('Setting current directory to: {}'.format(scriptdir))
    os.chdir(scriptdir)

    # pre-initialize core
    core.em_core.get_core_instance()

    mainret = 0
    if args.gui == 'qt':
        from gui_qt import main as gui_main
        mainret = gui_main.start_gui()

    logger.debug('Graceful shutdown.')
    logging.shutdown()  # this flushes buffers and closes all log handlers
    return mainret


if __name__ == '__main__':
    sys.exit(main())
