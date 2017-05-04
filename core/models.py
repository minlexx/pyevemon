# -*- coding: utf-8 -*-
"""
Models for SQLAlchemy
"""

from enum import IntEnum, unique
import re

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr


@unique
class EveApiAccessMask(IntEnum):
    AccountBalance         = 1
    AssetList              = 2
    CalendarEventAttendees = 4
    CharacterSheet         = 8
    ContactList            = 16
    ContactNotifications   = 32
    FacWarStats            = 64
    IndustryJobs           = 128
    KillLog                = 256
    MailBodies             = 512
    MailingLists           = 1024
    MailMessages           = 2048
    MarketOrders           = 4096
    Medals                 = 8192
    Notifications          = 16384
    NotificationTexts      = 32768
    Research               = 65536
    SkillInTraining        = 131072
    SkillQueue             = 262144
    Standings              = 524288
    UpcomingCalendarEvents = 1048576
    Walletjournal          = 2097152
    WalletTransactions     = 4194304
    CharacterInfo_public   = 8388608
    CharacterInfo_private  = 16777216
    AccountStatus          = 33554432
    Contracts              = 67108864
    Locations              = 134217728
    Bookmarks              = 268435456
    ChatChannels           = 536870912
    Skills                 = 1073741824
    Clones                 = 2147483648


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
    key_type = Column(String(32))
    access_mask = Column(Integer)
    expire_ts = Column(Integer)

    def __init__(self, keyid: str='', vcode: str='', friendly_name: str=''):
        self.keyid = keyid
        self.vcode = vcode
        self.friendly_name = friendly_name
        # fields below are not stored in DB
        self.characters = {}
        self.expired = False

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
        return 'EmApiKey({}, "{}")'.format(self.keyid, self.vcode)

    def __eq__(self, other) -> bool:
        """
        Api keys compare equal when their keyids are equal
        :param other: other EmApiKey object
        :return: True, if other object has the same keyid as me.
        """
        if isinstance(other, EmApiKey):
            if other.keyid == self.keyid:
                return True
        return False
