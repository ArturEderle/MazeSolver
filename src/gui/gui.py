from tkinter import Tk, BOTH, Canvas
from src.models.geometry import Line
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
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

    def draw_cell(self, cell, fill_color):
        if cell.has_left_wall:
            left_wall_line = Line(cell.get_top_left(), cell.get_bottom_left())
            self.draw_line(left_wall_line, fill_color)
        if cell.has_right_wall:
            right_wall_line = Line(cell.get_top_right(), cell.get_bottom_right())
            self.draw_line(right_wall_line, fill_color)
        if cell.has_top_wall:
            top_wall_line = Line(cell.get_top_left(), cell.get_top_right())
            self.draw_line(top_wall_line, fill_color)
        if cell.has_bottom_wall:
            bottom_wall_line = Line(cell.get_bottom_left(), cell.get_bottom_right())
            self.draw_line(bottom_wall_line, fill_color)
        self._animate()

    def draw_maze(self, maze, cells_color):
        for row in maze.get_cells():
            for cell in row:
                self.draw_cell(cell, cells_color)

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
        time.sleep(0.05)

