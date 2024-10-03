# importing from the module
from unittest import TestCase # here TestCase is in Pascal Case
from triangle import area_of_a_triangle

# creating the class with TestCase as a Base Class
class TestArea(TestCase):
    # NOTE: Setup & Teardown methods are mandatory

    def test_float_value(self):
        # below is the DocString
        """test area for float values"""
        # happy paths
        self.assertAlmostEqual(area_of_a_triangle(3.4556, 8.3567), 14.43870626)
        self.assertEqual(area_of_a_triangle(2.3, 5.7), 6.555)

    def test_integer_values(self):
        # INFO: via docstring doctest can also be done
        """Test area for integer values"""
        self.assertEqual(area_of_a_triangle(2, 5), 5.0)
        self.assertEqual(area_of_a_triangle(4, 6), 12.0)
    
    def test_zero_base(self):
        """ Test areas when base is zero """
        self.assertEqual(area_of_a_triangle(0, 5), 0.0)

    def test_zero_height(self):
        """ Test areas when height is zero """
        self.assertEqual(area_of_a_triangle(2, 0), 0.0)

    def test_zero_values(self):
        """ Test areas when base and height are zero """
        self.assertEqual(area_of_a_triangle(0, 0), 0.0)

    def test_negative_base(self):
        """ Test that ValueError is raised when base is negative """
        self.assertRaises(ValueError, area_of_a_triangle, -2, 5)

    def test_negative_height(self):
        """ Test that ValueError is raised when height is negative """
        self.assertRaises(ValueError, area_of_a_triangle, 2, -5)

    def test_negative_values(self):
        """ Test that ValueError is raised when both are negative """
        self.assertRaises(ValueError, area_of_a_triangle, -2, -5)

    def test_with_boolean(self):
        """ Test that TypeError is raised with boolean types """
        self.assertRaises(TypeError, area_of_a_triangle, True, 5)   # test booleans
        self.assertRaises(TypeError, area_of_a_triangle, 2, True)

    def test_with_string(self):
        """ Test that TypeError is raised with string types """
        self.assertRaises(TypeError, area_of_a_triangle, "base", 5) # test strings
        self.assertRaises(TypeError, area_of_a_triangle, 2, "height")

    def test_with_nulls(self):
        """ Test that TypeError is raised with null types """
        self.assertRaises(TypeError, area_of_a_triangle, None, 5) # test strings
        self.assertRaises(TypeError, area_of_a_triangle, 2, None)
