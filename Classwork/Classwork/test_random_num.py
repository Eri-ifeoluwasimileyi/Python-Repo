import unittest
from random_num import *

class TestRandom(unittest.TestCase):

    def test_that_random_number_exist(self):
        random_number(list)

    def test_that_length_of_num_is_valid(self):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4]
        self.assertEqual(10, length_of_number(list))


    def test_that_even_num_is_valid(self):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4]
        self.assertEqual(22, even_number(list))  # add assertion here


    def test_that_odd_num_is_valid(self):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4]
        self.assertEqual(28, odd_number(list))  # add assertion here


    def test_that_multiply_num_is_valid(self):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4]
        self.assertEqual(56, multiply(list))  # add assertion here


    def test_that_average_num_is_valid(self):
        list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 4]
        self.assertEqual(5, average_of_number(list))  # add assertion here
