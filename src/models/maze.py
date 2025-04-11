from src.models.geometry import Cell, Point
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__wall_length = cell_size_x + cell_size_y
        self.__win = win
        self.__cells = [[] for _ in range(num_rows)]
        self._create_cells()
        random.seed(seed)

    def _create_cells(self):
        if self.__num_rows < 2 or self.__num_cols < 2:
            raise ValueError('Mazes must have at least 2 rows and 2 cols')
        if self.__x1 < 0 or self.__y1 < 0:
            raise ValueError('Maze cannot have negative x1 and y1')
        if self.__cell_size_x < 0 or self.__cell_size_y < 1:
            raise ValueError('Maze cannot have cells with negative cell sizes')
        wall_length = self.__wall_length
        x = self.__x1
        for col in range(0, self.__num_cols):
            y = self.__y1
            for row in range(0, self.__num_rows):
                p1 = Point(x, y)
                p2 = Point(x + wall_length, y + wall_length)
                new_cell = Cell(p1, p2)
                self.__cells[row].append(new_cell)
                y += wall_length
            x += wall_length

    def break_entrance_and_exit(self):
        entrance_cell = self.get_cells()[0][0]
        exit_cell = self.get_cells()[-1][-1]
        entrance_cell.has_bottom_wall = False
        entrance_cell.has_left_wall = False
        entrance_cell.has_right_wall = False
        exit_cell.has_top_wall = False
        exit_cell.has_left_wall = False
        exit_cell.has_right_wall = False
        return entrance_cell, exit_cell

    def break_walls_r(self, i, j, window, cell_color):
        # mark current cell as visited
        current_cell = self.get_cells()[i][j]
        current_cell.visited = True
        # erase color (background color)
        erase_color = "white"

        while True:
            # Create a new empty list to hold the i and j values you will need to visit
            queue = []
            # Discover Neighbors
            # Check Top Neighbor exists; visited If not add to queue
            if i > 0 and not self.__cells[i - 1][j].visited:
                queue.append((i - 1, j, "top"))
            # Check Bottom Neighbor exists; visited If not add to queue
            if i < self.__num_rows - 1 and not self.__cells[i + 1][j].visited:
                queue.append((i + 1, j, "bottom"))
            # Check Left Neighbor exists; visited If not add to queue
            if j > 0 and not self.__cells[i][j - 1].visited:
                queue.append((i, j - 1, "left"))
            # Check Right Neighbor exists; visited If not add to queue
            if j < self.__num_cols - 1 and not self.__cells[i][j + 1].visited:
                queue.append((i, j + 1, "right"))
            # No Direction to go
            if len(queue) == 0:
                return
            # Pick a random direction (random cell inside the queue)
            neighbor_i, neighbor_j, direction = random.choice(queue)
            queue.remove((neighbor_i, neighbor_j, direction))
            match direction:
                case "top":
                    current_cell.open_top_wall()
                    window.draw_cell(current_cell, erase_color)
                case "bottom":
                    current_cell.open_bottom_wall()
                    window.draw_cell(current_cell, erase_color)
                case "left":
                    current_cell.open_left_wall()
                    window.draw_cell(current_cell, erase_color)
                case "right":
                    current_cell.open_right_wall()
                    window.draw_cell(current_cell, erase_color)
            # Recursion on next element in queue
            self.break_walls_r(neighbor_i, neighbor_j, window, cell_color)

    def reset_cells_visited(self):
        for row in self.get_cells():
            for cell in row:
                cell.visited = False

    def get_cells(self):
        return self.__cells