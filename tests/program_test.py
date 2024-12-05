import unittest
from unittest import mock
from os.path import join

from project1.program import CoolProg


class TestCoolProg(unittest.TestCase):
    def test_bubble_sort(self):
        my_prog = CoolProg()
        my_prog.bubblesort()
        self.assertEqual(["three", "tuth", "two"], my_prog.list)


if __name__ == "__main__":
    unittest.main()
