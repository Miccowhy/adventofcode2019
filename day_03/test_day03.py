import unittest

from day_03 import day03


class Example1Test(unittest.TestCase):
    def setUp(self):
        self.wires = day03.unpack_paths("""R8,U5,L5,D3
U7,R6,D4,L4""")

    def test_task1(self):
        self.assertEqual(6, day03.closest_manhattan_distance(self.wires[0], self.wires[1]))

    def test_task2(self):
        self.assertEqual(30, day03.step_count(self.wires[0], self.wires[1]))


class Example2Test(unittest.TestCase):

    def setUp(self):
        self.wires = day03.unpack_paths("""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""")

    def test_task1(self):
        self.assertEqual(159, day03.closest_manhattan_distance(self.wires[0], self.wires[1]))

    def test_task2(self):
        self.assertEqual(610, day03.step_count(self.wires[0], self.wires[1]))


class Example3Test(unittest.TestCase):

    def setUp(self):
        self.wires = day03.unpack_paths("""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""")

    def test_task1(self):
        self.assertEqual(135, day03.closest_manhattan_distance(self.wires[0], self.wires[1]))

    def test_task2(self):
        self.assertEqual(410, day03.step_count(self.wires[0], self.wires[1]))
