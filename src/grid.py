class Grid:
    def __init__(self, rows, cols, obstacles, start, goal):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.start = start
        self.goal = goal

    def is_valid(self, position):
        row, col = position

        if row < 0 or row >= self.rows:
            return False

        if col < 0 or col >= self.cols:
            return False

        if position in self.obstacles:
            return False

        return True

    def get_neighbors(self, position):
        row, col = position

        possible_moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        neighbors = []

        for row_move, col_move in possible_moves:
            new_position = (
                row + row_move,
                col + col_move
            )

            if self.is_valid(new_position):
                neighbors.append(new_position)

        return neighbors