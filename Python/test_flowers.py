import unittest
from flowers import petals

class TestFlowers(unittest.TestCase):

	def test_that_petals_function_only_takes_number(self):

		try:
			int("beny")
			self.fail("Allowed")
		except ValueError:
			print("Only numbers are accepted")
	def test_that_petals_function_return_boolean(self):

		actual = petals(4)
		expected = True
		self.assertEqual(actual, expected)