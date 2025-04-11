from src.models.geometry import Cell, Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
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

    def get_cells(self):
        return self.__cells