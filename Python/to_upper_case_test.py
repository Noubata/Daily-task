import unittest
from to_upper_case import the_upper_case

class TestToUpperCase(unittest.TestCase):

	def test_that_the_input_returns_uppercase(self):
		
		actual = the_upper_case('Beny') 
		expected = "Beny"
		self.assertEqual(actual, expected)
	