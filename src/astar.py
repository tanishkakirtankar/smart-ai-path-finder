import heapq


def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def astar(grid):
    start = grid.start
    goal = grid.goal

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    parent = {
        start: None
    }

    cost = {
        start: 0
    }

    nodes_explored = 0

    while priority_queue:

        current_cost, current = heapq.heappop(priority_queue)
        nodes_explored += 1

        if current == goal:
            break

        for neighbor in grid.get_neighbors(current):

            new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (priority, neighbor)
                )

                parent[neighbor] = current

    if goal not in parent:
        return None, nodes_explored

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, nodes_explored