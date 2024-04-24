""" 
Iterative version of Floyd Algorithm from the PDF given
to test against the updated recursive version.
"""

import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 5, NO_PATH, 10],
[NO_PATH, 0, 3, NO_PATH],
[NO_PATH, NO_PATH, 0, 1],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def iterative_floyd(distance):
    """ 
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node,end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                distance[start_node][intermediate] + distance[intermediate][end_node] )
    #Any value that have sys.maxsize has no path
   # print (distance)
    #return updated distance
    return distance
iterative_floyd(graph)
