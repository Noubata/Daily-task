import unittest
from to_upper_case import the_upper_case

class TestToUpperCase(unittest.TestCase):

	def test_that_the_input_is_a_string(self):
		
		actual = the_upper_case("tt") 
		expected = "tt"
		self.assertEqual(actual, expected)