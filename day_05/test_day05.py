from unittest.mock import patch
from unittest import TestCase
import io
import sys

from day_05 import day05


class Task1Test(TestCase):
    def test_output_passed_input(self):
        data = [3, 0, 4, 0, 99]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data, 7)
        sys.stdout = sys.__stdout__

        self.assertEqual(7, int(captured_output.getvalue()))

    def test_task1(self):
        data = [1101, 100, -1, 4, 0]
        day05.intcode(data)
        self.assertEqual(99, data[4])


class Task2Test(TestCase):
    def test_equal_8_position(self):
        data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), 7)
        day05.intcode(data.copy(), 8)
        day05.intcode(data.copy(), 9)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(0, return_value[0])
        self.assertEqual(1, return_value[1])
        self.assertEqual(0, return_value[2])

    def test_less_than_8_position(self):
        data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), 7)
        day05.intcode(data.copy(), 8)
        day05.intcode(data.copy(), 9)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(1, return_value[0])
        self.assertEqual(0, return_value[1])
        self.assertEqual(0, return_value[2])

    def test_equal_8_immediate(self):
        data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), 7)
        day05.intcode(data.copy(), 8)
        day05.intcode(data.copy(), 9)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(0, return_value[0])
        self.assertEqual(1, return_value[1])
        self.assertEqual(0, return_value[2])

    def test_less_than_8_immediate(self):
        data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), 7)
        day05.intcode(data.copy(), 8)
        day05.intcode(data.copy(), 9)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(1, return_value[0])
        self.assertEqual(0, return_value[1])
        self.assertEqual(0, return_value[2])

    def test_jump_position(self):
        data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), -1)
        day05.intcode(data.copy(), 0)
        day05.intcode(data.copy(), 1)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(1, return_value[0])
        self.assertEqual(0, return_value[1])
        self.assertEqual(1, return_value[2])

    def test_jump_immediate(self):
        data = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), -1)
        day05.intcode(data.copy(), 0)
        day05.intcode(data.copy(), 1)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(1, return_value[0])
        self.assertEqual(0, return_value[1])
        self.assertEqual(1, return_value[2])

    def test_long_equal_8(self):
        data = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        day05.intcode(data.copy(), 7)
        day05.intcode(data.copy(), 8)
        day05.intcode(data.copy(), 9)
        sys.stdout = sys.__stdout__

        return_value = [int(value) for value in captured_output.getvalue().splitlines()]
        self.assertEqual(999, return_value[0])
        self.assertEqual(1000, return_value[1])
        self.assertEqual(1001, return_value[2])
