"""
Module for testing the performance of the recursive function in comparison to the iterative version.
Using timeit to create a test case to measure the time taken by each function.
"""
import timeit
import sys
from recursive_floyd import recursive_floyd_algorithm
from iterative_function import iterative_floyd

def test_performance():
    """ Test case for iterative function """
    graph_matrix = [
        [0, 5, sys.maxsize, 10],
        [sys.maxsize, 0, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0,   1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]

#record how long the recursive function takes to compute
    recursive_time = timeit.timeit(lambda: recursive_floyd_algorithm(graph_matrix), number=1000)

    #record how long the iterative function takes to compute
    iterative_time = timeit.timeit(lambda: iterative_floyd(graph_matrix), number=1000)

    print("Recursive time:", recursive_time)
    print("Iterative time:", iterative_time)

test_performance()
