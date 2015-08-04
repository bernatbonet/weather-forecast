import unittest
from weather import weather as w


class RunTest(unittest.TestCase):
    def test_1(self):
        city = 'Palma'
        w(city)

    def test_2(self):
        city = 'NewYork'
        w(city)

    def test_3(self):
        city = 'kjabfifnbweq'
        w(city)

if __name__ == '__main__':
    unittest.main()
