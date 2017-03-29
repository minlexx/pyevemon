"""
Models for SQLAlchemy
"""


class ApiKey(object):
    def __init__(self, keyid: str='', vcode: str=''):
        self.keyid = keyid
        self.vcode = vcode

    def __str__(self):
        return 'ApiKey({}, {})'.format(self.keyid, self.vcode)
