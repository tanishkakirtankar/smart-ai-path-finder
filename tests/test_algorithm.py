import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.grid import Grid
from src.bfs import bfs
from src.dfs import dfs
from src.astar import astar


def test_bfs():
    grid = Grid(
        3,
        3,
        {(1, 1)},
        (0, 0),
        (2, 2)
    )

    path, nodes = bfs(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

    print("BFS test passed")


def test_dfs():
    grid = Grid(
        3,
        3,
        {(1, 1)},
        (0, 0),
        (2, 2)
    )

    path, nodes = dfs(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

    print("DFS test passed")


def test_astar():
    grid = Grid(
        3,
        3,
        {(1, 1)},
        (0, 0),
        (2, 2)
    )

    path, nodes = astar(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

    print("A* test passed")


if __name__ == "__main__":
    test_bfs()
    test_dfs()
    test_astar()

    print("\nAll tests passed successfully!")