import unittest

from core.evedata import EVEData


class TestEveData(unittest.TestCase):

    def test_typeID(self):
        ed = EVEData()
        res = ed.find_typeid(3351)
        self.assertEqual(type(res), dict)
        self.assertEqual(res['groupID'], 258)
        self.assertEqual(res['typeName'], 'Shield Command Specialist')
        pass


if __name__ == '__main__':
    unittest.main()
