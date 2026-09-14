import time

from src.bfs import bfs
from src.dfs import dfs
from src.astar import astar


def run_algorithm(algorithm, grid):
    start_time = time.perf_counter()

    path, nodes_explored = algorithm(grid)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    if path:
        path_length = len(path) - 1
        path_found = "Yes"
    else:
        path_length = 0
        path_found = "No"

    return {
        "path": path,
        "path_found": path_found,
        "path_length": path_length,
        "nodes_explored": nodes_explored,
        "execution_time": execution_time
    }


def compare_algorithms(grid):
    results = {}

    results["BFS"] = run_algorithm(bfs, grid)

    results["DFS"] = run_algorithm(dfs, grid)

    results["A*"] = run_algorithm(astar, grid)

    return results


def print_comparison(results):
    print("\n" + "=" * 65)
    print("           ALGORITHM COMPARISON RESULTS")
    print("=" * 65)

    for name, result in results.items():

        print(f"\n{name}")

        print("-" * 40)

        print(f"Path Found: {result['path_found']}")
        print(f"Path Length: {result['path_length']}")
        print(f"Nodes Explored: {result['nodes_explored']}")
        print(
            f"Execution Time: "
            f"{result['execution_time']:.6f} seconds"
        )

    print("\n" + "=" * 65)

def print_recommendation(results):
    bfs_result = results["BFS"]
    dfs_result = results["DFS"]
    astar_result = results["A*"]

    print("\n" + "=" * 65)
    print("              AI RECOMMENDATION")
    print("=" * 65)

    shortest_length = min(
        bfs_result["path_length"],
        dfs_result["path_length"],
        astar_result["path_length"]
    )

    print(
        f"\nShortest Path Length Found: {shortest_length}"
    )

    print("\nAnalysis:")

    if bfs_result["path_length"] == shortest_length:
        print(
            "- BFS found an optimal shortest path "
            "in the unweighted grid."
        )

    if dfs_result["path_length"] > shortest_length:
        print(
            "- DFS found a valid path but it was "
            "longer than the shortest path."
        )

    if astar_result["path_length"] == shortest_length:
        print(
            "- A* found an optimal path using "
            "heuristic information."
        )

    print("\nRecommendation:")

    if astar_result["path_length"] == shortest_length:
        print(
            "A* is recommended because it uses heuristic "
            "information to guide the search toward the goal."
        )
    else:
        print(
            "BFS is recommended because it found "
            "the shortest path."
        )

    print("=" * 65)