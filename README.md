# AI Smart Path Finder

## Overview

AI Smart Path Finder is a Python-based project that finds a path between a start position and a goal position in a grid environment containing obstacles.

The project implements and compares three Artificial Intelligence search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search Algorithm

The user can select an algorithm through an interactive command-line menu and view the generated path, path length, nodes explored, and execution time.

---

## Problem Statement

Finding an efficient path from a start position to a goal position is a common problem in Artificial Intelligence.

The objective of this project is to implement different search algorithms and compare their performance in a grid environment containing obstacles.

---

## Features

- Grid-based environment
- Start and goal positions
- Obstacles in the environment
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search Algorithm
- Path visualization
- Path length calculation
- Nodes explored calculation
- Execution time comparison
- Algorithm comparison
- Automatic recommendation

---

## Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores nodes level by level using a queue.

For an unweighted grid, BFS can find the shortest path.

### 2. Depth-First Search (DFS)

DFS explores one path deeply before backtracking.

DFS uses a stack and can find a valid path, but the path may not always be the shortest.

### 3. A* Search

A* uses the following evaluation function:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the actual cost from the start node.
- `h(n)` is the estimated cost to the goal.
- `f(n)` is the total estimated cost.

The project uses Manhattan Distance as the heuristic.

---

## Grid Symbols

```text
S = Start
G = Goal
# = Obstacle
. = Empty Cell
* = Path
```

---

## Project Structure

```text
smart-ai-path-finder/
│
├── main.py
├── README.md
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

---

## Requirements

- Python 3.x

No external Python libraries are required.

The project uses only Python standard libraries.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tanishkakirtankar/smart-ai-path-finder.git
```

Move into the project directory:

```bash
cd smart-ai-path-finder
```

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

## Example Results

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

Execution time may vary depending on the system.

---

## Running Tests

Run the following command:

```bash
python tests/test_algorithm.py
```

Expected output:

```text
BFS test passed
DFS test passed
A* test passed

All tests passed successfully!
```

---

## AI Concepts Used

This project applies the following Artificial Intelligence concepts:

- State Space Search
- Problem Solving Agents
- Uninformed Search
- Informed Search
- Breadth-First Search
- Depth-First Search
- A* Search
- Heuristic Function
- Manhattan Distance
- Path Finding

---

## Conclusion

This project demonstrates how different AI search algorithms behave in the same grid environment.

BFS and A* found the shortest path in the implemented environment, while DFS found a valid but longer path.

The project compares uninformed and informed search techniques using path length, nodes explored, and execution time.
