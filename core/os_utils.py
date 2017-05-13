# -*- coding: utf-8 -*-
import pathlib
import os
import os.path
import sys


def get_user_home_directory() -> str:
    path = os.path.expanduser('~')
    if path == '~':  # If the expansion fails, the path is returned unchanged.
        raise RuntimeError('Cannot detect your user home directory!')
    p = pathlib.Path(path)
    # Return a string representation of the path with forward slashes (/):
    return p.as_posix()


def get_savedata_directory() -> str:
    if sys.platform == 'win32':  # returns 'win32' also for 64-bit python
        if 'APPDATA' in os.environ:
            sdir = os.environ['APPDATA']
        else:
            sdir = os.environ['USERPROILE']
        sdir += '\\pyevemon'
    elif sys.platform == 'linux':
        # follow freedesktop XDG specification
        if 'XDG_CONFIG_HOME' in os.environ:
            sdir = os.environ['XDG_CONFIG_HOME']
            sdir += '/pyevemon'  # /home/user/.config/pyevemon
        else:
            sdir = os.environ['HOME']
            # try common config location
            if os.path.isdir(sdir + '/.config'):
                sdir += '/.config/pyevemon'  # /home/user/.config/pyevemon
            else:
                sdir += '/.pyevemon'          # /home/user/.pyevemon
    else:
        raise RuntimeError('Cannot detect your OS!')
    # create save directory if it does not exist
    p = pathlib.Path(sdir)
    if not (p.exists() and p.is_dir()):
        p.mkdir(parents=True)
    # Return a string representation of the path with forward slashes (/):
    return p.as_posix()


def get_program_directory() -> str:
    #  .../qevemon/core/os_utils.py => .../qevemon/core => .../qevemon
    s = pathlib.Path(__file__).parent.parent.as_posix()
    return s


def get_logs_directory() -> str:
    sdir = get_savedata_directory()
    sdir += '/logs'
    # create save directory if it does not exist
    p = pathlib.Path(sdir)
    if not (p.exists() and p.is_dir()):
        p.mkdir(parents=True)
    # Return a string representation of the path with forward slashes (/):
    return p.as_posix()
