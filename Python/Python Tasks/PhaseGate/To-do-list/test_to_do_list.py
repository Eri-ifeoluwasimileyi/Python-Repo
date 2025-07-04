import to_do_list
import unittest
#from unittest import TestCase


class TestList(unittest.TestCase):

	
	def test_that_to_do_list_was_created(self):
		list = []

		to_do_list.add_a_task(list, "yam")
	
	
	def test_that_add_a_task_exist(self):
		list = []

		actual = to_do_list.add_a_task(list, "yam")
		expected = "task added"
		self.assertEqual(actual, expected)


	def test_that_add_a_task_can_append(self):
		list = []

		actual = to_do_list.add_a_task(list, "wash, cook, bath, eat")
		expected = "task added"
		self.assertEqual(actual, expected)


	def test_mark_complete_is_valid(self):
		list = []
		to_do_list.add_a_task(list, "wash")

		actual = to_do_list.mark_complete(list, "1")
		expected = "marked"
		self.assertEqual(actual, expected)


	def test_mark_complete_is_can_take_int(self):
		list = []
		to_do_list.add_a_task(list, "3")

		actual = to_do_list.mark_complete(list, "1")
		expected = "marked"
		self.assertEqual(actual, expected)


	def test_mark_complete_is_cannot_take_string(self):
		list = []
		to_do_list.add_a_task(list, "eriife")

		actual = to_do_list.mark_complete(list, "erifemi")
		expected = "invalid input"
		self.assertEqual(actual, expected)


	def test_delete_task_is_valid(self):
		list = []
		to_do_list.add_a_task(list, "yam")

		actual = to_do_list.delete_task(list, "1")
		expected = "deleted successfuly"
		self.assertEqual(actual, expected)


	def test_delete_task_is_cannot_take_string(self):
		list = []
		to_do_list.add_a_task(list, "eriife")

		actual = to_do_list.delete_task(list, "erifemi")
		expected = "invalid input"
		self.assertEqual(actual, expected)


	def test_delete_task_is_can_take_int(self):
		list = []
		to_do_list.add_a_task(list, "2")

		actual = to_do_list.delete_task(list, "1")
		expected = "deleted successfuly"
		self.assertEqual(actual, expected)




