import unittest

from core.evedata import EVEData


class TestEveData(unittest.TestCase):

    def setUp(self):
        self.evedata = EVEData()

    def tearDown(self):
        del self.evedata

    def test_typeID(self):
        res = self.evedata.find_typeid(3351)
        self.assertEqual(type(res), dict)
        self.assertEqual(res['groupID'], 258)
        self.assertEqual(res['typeName'], 'Shield Command Specialist')


if __name__ == '__main__':
    unittest.main()
