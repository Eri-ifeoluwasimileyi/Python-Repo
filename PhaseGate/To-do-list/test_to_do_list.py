import to_do_list
import unittest
#from unittest import TestCase


class TestList(unittest.TestCase):

	
	def test_that_to_do_list_was_created(self):
		actual = 1
		expected = 1
		self.assertEqual(actual, expected)
	
	
	def test_that_add_a_task_exist(self):
		list = []
		actual = to_do_list.add_a_task(list, "yam")
		expected = "added"
		self.assertEqual(actual, expected)

"""
	def test_view_all_tasks_is_valid(self):
		list = []
		to_do_list.add_a_task(list, "yam")
		actual = to_do_list.view_all_tasks(list)
		expected = "yam"
		self.assertEqual(actual, expected)
"""