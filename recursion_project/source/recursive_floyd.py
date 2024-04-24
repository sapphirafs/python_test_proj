""" Implement a recursive version of Floyd's algorithm """
import sys

#if no path eists the maximum value is assigned
NO_PATH = sys.maxsize


def recursive_floyd_algorithm(graph):
    """
    The function starts the recursion proccess to utilise the Floyd algorithm
    to find the shortest path between four nodes using recursion,
    by invoking the inner function with the graph parameter.
    Parameter:
         graph (list of lists (2D array)) containting integers).
          Entries [i][j] represent the value of distance between nodes, i and j.
    Returns:
         value is returned by inner recursive function 
          that finds the quickest route between the four nodes in the graph.
    """
    max_length = len(graph)

    def find_quickest_route(dist, intermediate, i, j):
        """ 
        A recursive helper function to go through each node in the graph
          and return updated values for distance between nodes.
        Parameters: 
                dist(list of lists with the lowest possible route values between node pairs), 
                intermediate(int), 
                i(int): start node, 
                j(int): end node.
        Returns: 
                (list of lists) The function calls itself 
                    to return a new list of lists with the lowest possible path values.
                It iterates though recursively until all the quickest routes are found.

        """
        #base cases
        if i == max_length:
            #if all nodes are proccessed then return the distance graph matrix
            # as all of the shortest paths are now found.
            #distance is the matrix(list of lists).
            return dist
        if j == max_length:
            #if all possible end nodes for the current start node have reached the end of the graph,
            #move to the next statring node and set the end_node index to 0 again.
            return find_quickest_route(dist, intermediate, i + 1, 0)
        if intermediate == max_length:
            #As the intermediate node has reached its limit,
            #move to the next end node for more possible paths.
            return find_quickest_route(dist, 0, i, j + 1)
        #the statements below find the values of the connections from node to node).
        if i == j:
            dist[i][j] = 0
            #if the distance between the start and end node
            #with the intervention of the intermediate,
            #is shorter then going from start to end,
            #update the the distance matrix with this shorter distance.
        elif dist[i][intermediate] + dist[intermediate][j] < dist[i][j]:
            dist[i][j] = dist[i][intermediate] + dist[intermediate][j]
            #Function recursively calls itself with the current values as arguments to the params.
            #The intermediate node index is incremented to move to the next node in the matrix.
            #This recursion continues until all combinations are tried,
            #to find the quickest path between node pairs.
        return find_quickest_route(dist, intermediate + 1, i, j)

    #Create the matrix using the 2d graph array by itterating through the rows in the graph array.
    #The changes made to the distance 2d array wont change the initial graph variable,
    #this is because it includes a slice (row[:]) that creates a
    #copy of the graph rows to be referenced.
    distance = [row[:] for row in graph]

    # Begin recursion and call the helper function with lowest values for the routes as arguments.
    return find_quickest_route(distance, 0, 0, 0)

# Example usage:
graph_matrix = [
    [0, 5, NO_PATH, 10],
    [NO_PATH, 0, 3, NO_PATH],
    [NO_PATH, NO_PATH, 0, 1],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# matrix = recursive_floyd_algorithm(graph_matrix)
# for array in matrix:
#     print(array)
