import unittest

from src.models.maze import Maze


class MazeTest(unittest.TestCase):

    def test_initialization(self):
        maze = Maze(0, 0, 5, 5, 10, 10, False)
        self.assertIsNotNone(maze)

    def test_maze_create_cells(self):
        x1 = 50
        y1 = 50
        cell_size_x = 0
        cell_size_y = 50
        num_rows = 10
        num_cols = 14
        maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, False)
        cells = maze.get_cells()
        self.assertEqual(len(cells), num_rows)
        self.assertEqual(len(cells[0]), num_cols)

    def test_cell_values(self):
        maze = Maze(0, 0, 5, 5, 10, 10, False)
        cells = maze.get_cells()
        self.assertIsNotNone(cells[0][0])
        self.assertIsNotNone(cells[4][4])

    def test_invalid_cell_size_raises_exception(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 5, -10, 20, False)

    def test_too_few_rows_cols_raises_exception(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 1, 1, 10, 10, False)

    def test_negative_start_coordinates_raise_exception(self):
        with self.assertRaises(ValueError):
            Maze(-5, -5, 5, 5, 10, 10, False)

    def test_all_cells_are_initialized(self):
        maze = Maze(0, 0, 5, 5, 10, 10, False)
        cells = maze.get_cells()
        for row in cells:
            for cell in row:
                self.assertIsNotNone(cell)


if __name__ == '__main__':
    unittest.main()
