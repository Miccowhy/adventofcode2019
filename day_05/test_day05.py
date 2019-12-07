import unittest

from day_05 import day05


class Task1Test(unittest.TestCase):
    def setUp(self):
        self.data = [1101, 100, -1, 4, 0]

    def test_task1(self):
        day05.intcode(self.data)
        self.assertEqual(99, self.data[4])

