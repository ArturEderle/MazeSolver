from tkinter import Tk, BOTH, Canvas
from src.models.geometry import Line
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height, background="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__canvas.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color):
        self.__canvas.create_line(line.point1.x, line.point1.y, line.point2.x, line.point2.y, fill=fill_color, width=2)

    def draw_cell(self, cell, cell_color):
        cell.draw(self, cell_color)
        self._animate()

    def draw_maze(self, maze, cells_color):
        for row in maze.get_cells():
            for cell in row:
                self.draw_cell(cell, cells_color)
        self.draw_break_entrance_and_exit(maze)
        exit_cell_i, exit_cell_j = len(maze.get_cells()) - 1, len(maze.get_cells()[0]) - 1
        maze.break_walls_r(exit_cell_i, exit_cell_j, self, cells_color)
        maze.reset_cells_visited()

    def draw_break_entrance_and_exit(self, maze):
        cells_color = "white"
        entrance_cell, exit_cell = maze.break_entrance_and_exit()
        self.draw_cell(entrance_cell, cells_color)
        self.draw_cell(exit_cell, cells_color)

    def draw_path_between_cells(self, cell1, cell2, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        path = Line(cell1.center_point(), cell2.center_point())
        self.draw_line(path, fill_color)

    def close(self):
        self.__running = False

    def _animate(self):
        self.redraw()
        time.sleep(0.03)

