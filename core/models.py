"""
Models for SQLAlchemy
"""

import re

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class EmAutoTableAndIdMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


EmModelBase = declarative_base()


class EmKeyValue(EmModelBase, EmAutoTableAndIdMixin):
    key = Column(String(256))
    value = Column(String(256))

    def __init__(self, key: str='', value: str=''):
        self.key = key
        self.value = value

    def __str__(self):
        return 'EmKeyValue("{}"="{}")'.format(self.key, self.value)


class EmApiKey(EmModelBase, EmAutoTableAndIdMixin):

    keyid = Column(String(32))
    vcode = Column(String(256))
    friendly_name = Column(String(256))

    def __init__(self, keyid: str='', vcode: str='', friendly_name: str=''):
        self.keyid = keyid
        self.vcode = vcode
        self.friendly_name = friendly_name

    def is_valid(self):
        if len(self.keyid) != 7: return False
        if len(self.vcode) != 64: return False
        # keyid contains only numbers
        r = re.match(r'^([0-9])+$', self.keyid)
        if r is None: return False
        # vcode can contain only numbers and EN letters
        r = re.match(r'^([0-9a-zA-Z])+$', self.vcode)
        if r is None: return False
        return True

    def is_empty(self):
        if self.keyid is None or self.keyid == '': return True
        if self.vcode is None or self.vcode == '': return True
        return False

    def __str__(self):
        return 'EmApiKey("{}", "{}")'.format(self.keyid, self.vcode)
