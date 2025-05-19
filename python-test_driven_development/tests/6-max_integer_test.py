#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""
    
    def test_max_integer(self):
        """Test normal cases where list has multiple integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([9, 3, 5, 7, 8]), 9)
    
    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_single_element(self):
        """Test single element list"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1]), -1)
    
    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-3, -1, -4, -2]), -1)
    
    def test_mixed_numbers(self):
        """Test list with both positive and negative numbers"""
        self.assertEqual(max_integer([1, -1, 0, 4]), 4)
    
    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([2.5, 1.5, 3.0]), 3.0)
    
    def test_mixed_types(self):
        """Test list with both integers and floats"""
        self.assertEqual(max_integer([2.5, 1, 3]), 3)
    
    def test_repeated_elements(self):
        """Test list with repeated maximum value"""
        self.assertEqual(max_integer([2, 3, 3, 1]), 3)
    
    def test_non_integer(self):
        """Test case where non-integer elements are passed"""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])  # mix of integers and string

if __name__ == '__main__':
    unittest.main()
