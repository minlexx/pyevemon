"""
Models for SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class EmAutoTableAndIdMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


EmModelBase = declarative_base()


class EmApiKey(EmModelBase, EmAutoTableAndIdMixin):

    keyid = Column(String(32))
    vcode = Column(String(256))
    friendly_name = Column(String(256))

    def __init__(self, keyid: str='', vcode: str='', friendly_name: str=''):
        self.keyid = keyid
        self.vcode = vcode
        self.friendly_name = friendly_name

    def is_valid(self):
        if len(self.keyid) != 7:
            return False
        if len(self.vcode) != 64:
            return False
        return True

    def __str__(self):
        return 'EmApiKey("{}", "{}")'.format(self.keyid, self.vcode)
