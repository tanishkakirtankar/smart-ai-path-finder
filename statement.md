# AI Smart Path Finder - Project Statement

## 1. Problem Statement

Finding an efficient path from a starting position to a target position is a common problem in Artificial Intelligence. In a grid environment containing obstacles, different search algorithms may explore the environment in different ways and may produce paths with different lengths and search costs.

The purpose of this project is to develop a command-line based AI Smart Path Finder that implements and compares Breadth-First Search (BFS), Depth-First Search (DFS), and A\* Search algorithms for finding a path between a start position and a goal position in an obstacle-based grid.

The system compares the algorithms using path length, number of nodes explored, and execution time.

## 2. Scope of the Project

The project focuses on path finding in a fixed grid environment.

The scope includes:

- Representing a grid as a search environment.
- Defining a start position and a goal position.
- Representing obstacles in the grid.
- Finding paths using BFS.
- Finding paths using DFS.
- Finding paths using A\* Search.
- Using Manhattan Distance as the heuristic for A\*.
- Displaying the generated path.
- Comparing the search algorithms.
- Measuring nodes explored and execution time.
- Providing an algorithm recommendation based on the comparison results.
- Testing the implemented search algorithms.

The project is implemented as a command-line application using Python and does not require a graphical user interface.

## 3. Target Users

The target users of this project are:

- Students learning Artificial Intelligence and search algorithms.
- Beginners who want to understand path-finding algorithms.
- Learners studying uninformed and informed search techniques.
- Users interested in comparing different AI search strategies.

## 4. High-Level Features

The major features of the system are:

1. Grid Environment
   - Represents the search space using rows and columns.
   - Supports obstacles, start position, and goal position.

2. BFS Path Finding
   - Uses Breadth-First Search to find a path.
   - Uses a queue for level-by-level exploration.

3. DFS Path Finding
   - Uses Depth-First Search to explore the search space.
   - Uses a stack for depth-first exploration.

4. A\* Path Finding
   - Uses the A\* search algorithm.
   - Uses the evaluation function f(n) = g(n) + h(n).
   - Uses Manhattan Distance as the heuristic.

5. Algorithm Comparison
   - Compares BFS, DFS, and A\*.
   - Displays path length, nodes explored, and execution time.

6. Path Visualization
   - Displays the discovered path directly on the grid.

7. AI Recommendation
   - Analyzes the results of the algorithms.
   - Provides a recommendation based on the shortest path and heuristic-guided search.

8. Algorithm Testing
   - Includes tests for BFS, DFS, and A\*.
