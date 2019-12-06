import unittest

from day_06 import day06


class Task1Test(unittest.TestCase):
    def setUp(self):
        data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
        day06.set_orbits(data)

    def test_task1(self):
        self.assertEqual(42, day06.task1_run())


class Task2Test(unittest.TestCase):
    def setUp(self):
        data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
        day06.set_orbits(data)

#    def test_task2(self):
#        self.assertEqual(42, day06.task1_run())
