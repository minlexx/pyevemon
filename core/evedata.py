# -*- coding: utf-8 -*-
import logging
import pathlib
import zipfile

import yaml

import core.os_utils
import core.logger


class EVEData:
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.datadir = core.os_utils.get_program_directory() + '/evedata'
        self._logger.debug('EVEData: using eve data dir: {}'.format(self.datadir))

        self.typeids = {}
        self.groupids = {}
        self._loaded = False

        self.load_sde()

    def load_sde(self):
        # 1. check that EVEdata dir exists
        p = pathlib.Path(self.datadir)
        if not (p.exists() and p.is_dir()):
            self._logger.error('EVE Data directory ({}) does not exist!'.format(self.datadir))
            return

        # 2. try to load extracted data from plain files
        try:
            fn = self.datadir + '/sde/fsd/groupIDs.yaml'
            with open(fn, mode='rt', encoding='utf-8') as f:
                self._logger.debug('Loading groupIDs...')
                self.groupids = yaml.load(f)
            fn = self.datadir + '/sde/fsd/typeIDs.yaml'
            with open(fn, mode='rt', encoding='utf-8') as f:
                self._logger.debug('Loading typeIDs...')
                self.typeids = yaml.load(f)
            self._loaded = True
        except IOError:
            pass

        if not self._loaded:
            # 3. try to load from zip maybe?
            self._logger.debug('Loading from extracted files failed, trying to find zip...')
            zips = sorted(p.glob('sde-*.zip'))
            if len(zips) == 0:
                self._logger.error('Cannot find ZIP SDE archive file '
                                   'and loading extracted data failed!')
                return
            latest_sde_path = zips[len(zips) - 1]
            self.load_sde_from_zip(latest_sde_path.as_posix())

        self._logger.debug('EVEData load complete.')

    def load_sde_from_zip(self, zip_file_path: str):
        self._logger.debug('Will load static EVE data from: {}'.format(zip_file_path))
        with zipfile.ZipFile(zip_file_path, mode='r') as zf:
            self._logger.debug('Loading groupIDs...')
            with zf.open('sde/fsd/groupIDs.yaml') as f:
                self.groupids = yaml.load(f)
            self._logger.debug('Loading typeIDs...')
            with zf.open('sde/fsd/typeIDs.yaml') as f:
                self.typeids = yaml.load(f)
        self._loaded = True
