"""
Module for testing resurion using Floyd Warshall's algorithm.
The Unit test has a test case to check that the funcion, recursive_floyd_algorithm,
works with different inputs. 
"""

import sys
import unittest
from recursive_floyd import recursive_floyd_algorithm
from iterative_function import iterative_floyd


class TestRecursion(unittest.TestCase):
    """
    This class inherits from unittest.TestCase 
    So every function in the class that begins with 'test' in the name,
    will be ran as a test.
    """
    def setUp(self):
        """Setup the state before the testing."""
        self.graph_matrix = [
             [0, 5, sys.maxsize, 10],
             [sys.maxsize, 0, 3, sys.maxsize],
             [sys.maxsize, sys.maxsize, 0,   1],
             [sys.maxsize, sys.maxsize, sys.maxsize, 0]
             ]
        #Predicted shortest path outpout
        #after running recursive_floyd_algorithm using graph_matix as input.
        self.prediction = [
            [0, 5, 8, 9],
            [sys.maxsize, 0, 3, 4],
            [sys.maxsize, sys.maxsize, 0, 1],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

    def tearDown(self):
        """Removes state after east test case."""
        pass

    def test_recursive_floyd_algorithm(self):
        """check for equal results"""
        result = recursive_floyd_algorithm(self.graph_matrix)
        self.assertEqual(result, self.prediction)

    def test_iterative_floyd(self):
        """check for equal results"""
        result = iterative_floyd(self.graph_matrix)
        self.assertEqual(result, self.prediction)
      # Add more test cases for edge cases, invalid input, etc.

if __name__ == '__main__':
    unittest.main()
