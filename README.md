# Recursion Project



## Directory Tree:

recursion_project <br>
├─docs <br>
│ └─requirements.txt <br>
├─source <br>
│ ├─__init__.py <br>
│ ├─iterative_function.py <br>
│ └─recursive_floyd.py <br>
├─tests <br>
│ ├─__init__.py <br>
│ ├─test_performance.py <br>
│ └─test_recursive_function.py <br>
└─README.md

## Description:

This package finds the shortest path between nodes in a graph matrix using using Floyd-Warshall algorithm and the inteperative Python language. 
A recursive function is implememnted and compared with the performance of an iterative function.

## How to Install:

1. Clone the repository: `git clone https://github.com/sapphirafs/recursion_project.git`
2. Navigate to the project directory: `cd shortest-path-finder`
3. Install the package: `pip install .`

## How to Run:

Follow these steps to use the functionalisty within your code:

1. Import the package in your Python code: `import shortest_path_finder`
2. Create a graph representing the weight values between vertices.
3. Call the `recursive_floyd(graph)` function whilst passing the graph matrix as an argument.
4. The function will return a matrix containing the shortest distances between every pair of vertices.

## For Example:

```python 
import recursion_project

# create the graph (2D array/list of lists)
graph = [
    [0, 5, sys.maxsize, 10],
    [sys.maxsize, 0, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

# Call and print the function
result = recursion_project.recursive_floyd(graph)
print(result)
