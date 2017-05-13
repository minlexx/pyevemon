# -*- coding: utf-8 -*-
import logging
import logging.handlers
import sys

import core.os_utils


_g_evemon_default_logger_level = logging.DEBUG
_g_evemon_console_log_handler = None
_g_evemon_rotating_log_handler = None
_g_evemon_unhandled_exception_logger = None
_g_evemon_unhandled_exception_handlers = []
_g_evemon_unhandled_exception_params = {}


def get_logger(tag: str) -> logging.Logger:
    global _g_evemon_default_logger_level
    global _g_evemon_console_log_handler
    global _g_evemon_rotating_log_handler

    # create formatter
    # formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s:%(funcName)s] %(message)s')

    # create console handler and set level to debug
    if _g_evemon_console_log_handler is None:
        _g_evemon_console_log_handler = logging.StreamHandler(stream=sys.stdout)
        _g_evemon_console_log_handler.setLevel(logging.NOTSET)  # display all
        _g_evemon_console_log_handler.setFormatter(formatter)

    if _g_evemon_rotating_log_handler is None:
        logs_dir = core.os_utils.get_logs_directory()
        _g_evemon_rotating_log_handler = logging.handlers.RotatingFileHandler(
            filename='{}/log.txt'.format(logs_dir),
            mode='a', encoding='utf-8', backupCount=5, maxBytes=10*1024*1024  # 10 Mb
        )
        _g_evemon_rotating_log_handler.setLevel(logging.NOTSET)
        _g_evemon_rotating_log_handler.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(tag)
    logger.setLevel(_g_evemon_default_logger_level)

    # add our global to logger
    logger.addHandler(_g_evemon_console_log_handler)
    logger.addHandler(_g_evemon_rotating_log_handler)
    return logger


def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    global _g_evemon_unhandled_exception_logger
    # call original excepthook if we got here somehow with no logger created
    if _g_evemon_unhandled_exception_logger is None:
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # Ignore KeyboardInterrupt so a console python program can exit with Ctrl + C
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # otherwise, log exception with our logger
    _g_evemon_unhandled_exception_logger.error('Unhandled exception:',
                                               exc_info=(exc_type, exc_value, exc_traceback))
    # call unhandled exception handlers
    global _g_evemon_unhandled_exception_handlers
    global _g_evemon_unhandled_exception_params
    for handler_func in _g_evemon_unhandled_exception_handlers:
        bound_param = None
        if handler_func in _g_evemon_unhandled_exception_params:
            bound_param = _g_evemon_unhandled_exception_params[handler_func]
        handler_func(bound_param, exc_type, exc_value, exc_traceback)


def init_unhandled_exception_handling(log_filename: str):
    global _g_evemon_unhandled_exception_logger
    if _g_evemon_unhandled_exception_logger is None:
        # create and setup logger
        # it will log to stderr and to a file specified by log_filename
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s: %(message)s')
        unhandled_exception_handler = logging.StreamHandler(stream=sys.stderr)
        unhandled_exception_handler.setLevel(logging.DEBUG)
        unhandled_exception_handler.setFormatter(formatter)
        uexh_file = logging.FileHandler(filename=log_filename, mode='a', encoding='utf-8', delay=True)
        uexh_file.setLevel(logging.DEBUG)
        uexh_file.setFormatter(formatter)
        _g_evemon_unhandled_exception_logger = logging.getLogger('UNHANDLED_EXCEPTION')
        _g_evemon_unhandled_exception_logger.setLevel(logging.DEBUG)
        _g_evemon_unhandled_exception_logger.addHandler(unhandled_exception_handler)
        _g_evemon_unhandled_exception_logger.addHandler(uexh_file)
    # override global unhandled exception handler with our handler
    sys.excepthook = handle_unhandled_exception


def add_unhandled_exception_handler(handler_func, bound_param):
    global _g_evemon_unhandled_exception_handlers
    global _g_evemon_unhandled_exception_params
    if handler_func not in _g_evemon_unhandled_exception_handlers:
        _g_evemon_unhandled_exception_handlers.append(handler_func)
        _g_evemon_unhandled_exception_params[handler_func] = bound_param


def remove_unhandled_exception_handler(handler_func):
    global _g_evemon_unhandled_exception_handlers
    global _g_evemon_unhandled_exception_params
    if handler_func in _g_evemon_unhandled_exception_handlers:
        _g_evemon_unhandled_exception_handlers.remove(handler_func)
        del _g_evemon_unhandled_exception_params[handler_func]
