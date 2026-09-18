# AI Smart Path Finder

## Overview

AI Smart Path Finder is a Python-based command-line application that finds a path between a start position and a goal position in a grid environment containing obstacles.

The project implements and compares three Artificial Intelligence search algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* A* Search Algorithm

The user can select an algorithm through an interactive command-line menu and view the generated path, path length, nodes explored, and execution time.

The project also compares all three algorithms and provides an automatic recommendation based on the obtained results.

---

## Problem Statement

Finding an efficient path from a start position to a goal position is a common problem in Artificial Intelligence.

The objective of this project is to implement different search algorithms and compare their behavior in a grid environment containing obstacles.

The algorithms are evaluated using:

* Path length
* Number of nodes explored
* Execution time

---

## Features

* Grid-based environment
* Start and goal positions
* Obstacles in the environment
* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* A* Search Algorithm
* Path visualization
* Path length calculation
* Nodes explored calculation
* Execution time measurement
* Algorithm comparison
* Automatic algorithm recommendation
* Algorithm testing
* Command-line execution without a graphical interface

---

## Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores nodes level by level using a queue.

Since the grid uses equal movement costs, BFS can find the shortest path when a path exists.

### 2. Depth-First Search (DFS)

DFS explores one path deeply before backtracking.

DFS uses a stack and can find a valid path, but it does not guarantee the shortest path.

### 3. A* Search

A* is an informed search algorithm that uses the following evaluation function:

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` is the actual cost from the start node.
* `h(n)` is the estimated cost from the current node to the goal.
* `f(n)` is the total estimated cost.

The project uses Manhattan Distance as the heuristic:

```text
h(n) = |x1 - x2| + |y1 - y2|
```

This heuristic is suitable for the four-direction movement used in the grid.

---

## Grid Symbols

```text
S = Start
G = Goal
# = Obstacle
. = Empty Cell
* = Path
```

The grid allows movement in four directions:

```text
        Up
        ↑
Left ← Cell → Right
        ↓
       Down
```

---

## Project Structure

```text
smart-ai-path-finder/
│
├── main.py
├── README.md
├── statement.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── grid.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── astar.py
│   └── comparison.py
│
└── tests/
    └── test_algorithm.py
```

### Module Description

| File                | Purpose                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| `main.py`           | Provides the command-line interface and runs the selected algorithm       |
| `grid.py`           | Defines the grid environment, obstacles, start, goal, and valid neighbors |
| `bfs.py`            | Implements Breadth-First Search                                           |
| `dfs.py`            | Implements Depth-First Search                                             |
| `astar.py`          | Implements A* Search using Manhattan Distance                             |
| `comparison.py`     | Compares the algorithms and generates a recommendation                    |
| `test_algorithm.py` | Tests the implemented search algorithms                                   |
| `statement.md`      | Contains the formal project statement, scope, target users, and features  |

---

## Requirements

* Python 3.x
* No external Python packages are required.

The project uses only Python standard libraries.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/tanishkakirtankar/smart-ai-path-finder.git
```

### 2. Move into the project directory

```bash
cd smart-ai-path-finder
```

No additional package installation is required.

---

## How to Run

Open Command Prompt or a terminal in the project directory and run:

```bash
python main.py
```

The following menu will appear:

```text
Choose an option:

1. Run BFS
2. Run DFS
3. Run A*
4. Compare All Algorithms
5. Exit
```

Enter a number between `1` and `5`.

---

## Algorithm Comparison

Selecting option `4` runs BFS, DFS, and A* on the same grid environment.

The comparison includes:

* Whether a path was found
* Path length
* Number of nodes explored
* Execution time

The system then provides an algorithm recommendation based on the comparison results.

---

## Example Results

The following results are from the sample grid used by the project. Execution time may vary depending on the computer and runtime environment.

### BFS

```text
Path Found: Yes
Path Length: 10
Nodes Explored: 20
```

### DFS

```text
Path Found: Yes
Path Length: 14
Nodes Explored: 16
```

### A*

```text
Path Found: Yes
Path Length: 10
Nodes Explored: 20
```

These values describe the behavior on the implemented sample grid and are not universal performance values for the algorithms.

---

## Running Tests

Run the following command from the project root:

```bash
python tests/test_algorithm.py
```

The test suite checks:

* BFS path finding
* DFS path finding
* A* path finding
* Correct start and goal positions
* Expected path lengths where applicable
* No-path scenarios

A successful execution should indicate that all implemented algorithm tests have passed.

---

## AI Concepts Used

This project applies the following Artificial Intelligence concepts:

* State Space Search
* Problem Solving Agents
* Uninformed Search
* Informed Search
* Breadth-First Search
* Depth-First Search
* A* Search
* Heuristic Function
* Manhattan Distance
* Path Finding
* Search Space Exploration
* Algorithm Performance Comparison

---

## System Architecture

The project follows a modular architecture:

```text
                    User
                      |
                      v
                  main.py
                      |
             Algorithm Selection
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
       BFS           DFS           A*
        |             |             |
        +-------------+-------------+
                      |
                      v
               Search Results
                      |
                      v
                comparison.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      Path Length  Nodes      Execution
                  Explored       Time
                      |
                      v
               Recommendation
```

The grid environment is managed by `grid.py`, while each search algorithm is implemented in a separate module.

---

## Limitations

* The current project uses a fixed grid environment.
* Movement is limited to four directions.
* All movement costs are equal.
* The application is command-line based.
* The project does not use a persistent database or external dataset.

---

## Future Enhancements

Possible future improvements include:

* Allowing users to create custom grids.
* Allowing users to enter their own start and goal positions.
* Supporting diagonal movement.
* Supporting weighted grids.
* Adding additional search algorithms such as Greedy Best-First Search.
* Providing graphical visualization of search exploration.
* Adding larger and dynamically generated environments.

---

## Project Statement

A detailed project statement containing the problem statement, scope, target users, and high-level features is available in:

```text
statement.md
```

---

## Conclusion

AI Smart Path Finder demonstrates how different Artificial Intelligence search algorithms behave when solving the same grid-based path-finding problem.

BFS and A* find a shortest path in the implemented unweighted grid, while DFS can find a valid path without guaranteeing that the path is shortest.

The project provides a practical comparison of uninformed and informed search techniques using path length, nodes explored, and execution time.

The implementation is modular, command-line executable, and includes tests for the implemented search algorithms.
