from src.grid import Grid
from src.bfs import bfs
from src.dfs import dfs
from src.astar import astar
from src.comparison import (
    run_algorithm,
    compare_algorithms,
    print_comparison,
    print_recommendation
)


def display_grid(grid, path=None):
    print("\nGRID:")

    for row in range(grid.rows):
        line = ""

        for col in range(grid.cols):
            position = (row, col)

            if position == grid.start:
                line += "S "

            elif position == grid.goal:
                line += "G "

            elif position in grid.obstacles:
                line += "# "

            elif path and position in path:
                line += "* "

            else:
                line += ". "

        print(line)


def print_result(name, result, grid):
    print("\n" + "=" * 50)
    print(f"{name} RESULT")
    print("=" * 50)

    print(f"Path Found: {result['path_found']}")
    print(f"Path Length: {result['path_length']}")
    print(f"Nodes Explored: {result['nodes_explored']}")
    print(
        f"Execution Time: "
        f"{result['execution_time']:.6f} seconds"
    )

    if result["path"]:
        print("\nPath:")
        print(result["path"])

        display_grid(grid, result["path"])


def main():

    rows = 6
    cols = 6

    obstacles = {
        (0, 3),
        (1, 1),
        (1, 3),
        (2, 1),
        (2, 4),
        (3, 3),
        (4, 1),
        (4, 4)
    }

    start = (0, 0)
    goal = (5, 5)

    grid = Grid(
        rows,
        cols,
        obstacles,
        start,
        goal
    )

    while True:

        print("\n" + "=" * 50)
        print("        AI SMART PATH FINDER")
        print("=" * 50)

        display_grid(grid)

        print("\nChoose an option:")
        print("1. Run BFS")
        print("2. Run DFS")
        print("3. Run A*")
        print("4. Compare All Algorithms")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            result = run_algorithm(bfs, grid)

            print_result(
                "BFS",
                result,
                grid
            )

        elif choice == "2":

            result = run_algorithm(dfs, grid)

            print_result(
                "DFS",
                result,
                grid
            )

        elif choice == "3":

            result = run_algorithm(astar, grid)

            print_result(
                "A*",
                result,
                grid
            )

        elif choice == "4":
            results = compare_algorithms(grid)
            print_comparison(results)
            print_recommendation(results)

        elif choice == "5":
            print("\nThank you for using AI Smart Path Finder!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()