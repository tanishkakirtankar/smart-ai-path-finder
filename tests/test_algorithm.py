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


def create_test_grid():
    return Grid(
        3,
        3,
        {(1, 1)},
        (0, 0),
        (2, 2)
    )


def test_bfs():
    grid = create_test_grid()

    path, nodes = bfs(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    assert len(path) - 1 == 4

    print("BFS test passed")


def test_dfs():
    grid = create_test_grid()

    path, nodes = dfs(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

    print("DFS test passed")


def test_astar():
    grid = create_test_grid()

    path, nodes = astar(grid)

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    assert len(path) - 1 == 4

    print("A* test passed")


def test_no_path():
    grid = Grid(
        3,
        3,
        {
            (0, 1),
            (1, 0),
            (1, 1)
        },
        (0, 0),
        (2, 2)
    )

    bfs_path, bfs_nodes = bfs(grid)
    dfs_path, dfs_nodes = dfs(grid)
    astar_path, astar_nodes = astar(grid)

    assert bfs_path is None
    assert dfs_path is None
    assert astar_path is None

    print("No-path test passed")


if __name__ == "__main__":
    test_bfs()
    test_dfs()
    test_astar()
    test_no_path()

    print("\nAll tests passed successfully!")
