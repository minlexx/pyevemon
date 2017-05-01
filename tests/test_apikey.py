# -*- coding: utf-8 -*-
import unittest

from core.models import EmApiKey


class TestEmApiKey(unittest.TestCase):

    def setUp(self):
        self.tests = []
        #  [ keyid  /  vcode  /  validity ]
        self.tests.append(('123',     'Lo8ocdCw0a1zDO2agyOEGiREaCpTbui1HZhl0SpgnzDw2vmaTBjUUmU9VuuBHo3z', False))
        self.tests.append(('1234567', 'Lo8ocdCw0a1zDO2agyOEGiREaCpTbui1HZhl0SpgnzDw2vmaTBjUUmU9VuuBHo3', False))
        self.tests.append(('1234567', 'Lo8ocdCw0a1zDO2agyOEGiREaCpTbui1HZhl0SpgnzDw2vmaTBjUUmU9VuuBHo3z', True))
        self.tests.append(('123456a', 'Lo8ocdCw0a1zDO2agyOEGiREaCpTbui1HZhl0SpgnzDw2vmaTBjUUmU9VuuBHo3z', False))
        self.tests.append(('1234567', 'Lo8ocdCw0a1zDO2agyOEGiREaCpTbui1HZhl0SpgnzDw2vmaTBjUUmU9VuuBHo3-', False))

    def test_validity(self):
        for t in self.tests:
            apikey = EmApiKey(t[0], t[1])
            self.assertEqual(apikey.is_valid(), t[2], str(apikey))


if __name__ == '__main__':
    unittest.main()
