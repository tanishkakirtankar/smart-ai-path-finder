def dfs(grid):
    start = grid.start
    goal = grid.goal

    stack = [start]
    visited = {start}

    parent = {
        start: None
    }

    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == goal:
            break

        for neighbor in grid.get_neighbors(current):

            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    if goal not in parent:
        return None, nodes_explored

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, nodes_explored