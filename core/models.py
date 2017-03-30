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


class EMApiKey(EmModelBase, EmAutoTableAndIdMixin):

    keyid = Column(String(32))
    vcode = Column(String(256))

    def __init__(self, keyid: str='', vcode: str=''):
        self.keyid = keyid
        self.vcode = vcode

    def __str__(self):
        return 'ApiKey({}, {})'.format(self.keyid, self.vcode)
