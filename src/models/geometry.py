
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

class Cell:
    def __init__(self, top_left=Point(50, 50), bottom_right=Point(100, 100)):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left = top_left
        self.__top_right = Point(bottom_right.x, top_left.y)
        self.__bottom_left = Point(top_left.x, bottom_right.y)
        self.__bottom_right = bottom_right
        self.__win = False
        self.visited = False

    def center_point(self):
        return Point((self.__top_left.x + self.__bottom_right.x) / 2, (self.__top_left.y + self.__bottom_right.y) / 2)

    def open_top_wall(self):
        self.has_top_wall = True
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_bottom_wall = False

    def open_left_wall(self):
        self.has_left_wall = True
        self.has_right_wall = False
        self.has_bottom_wall = False
        self.has_top_wall = False

    def open_right_wall(self):
        self.has_right_wall = True
        self.has_left_wall = False
        self.has_bottom_wall = False
        self.has_top_wall = False

    def open_bottom_wall(self):
        self.has_bottom_wall = True
        self.has_right_wall = False
        self.has_left_wall = False
        self.has_top_wall = False

    def draw(self, window, fill_color):
        if self.has_left_wall:
            left_wall_line = Line(self.get_top_left(), self.get_bottom_left())
            window.draw_line(left_wall_line, fill_color)
        if self.has_right_wall:
            right_wall_line = Line(self.get_top_right(), self.get_bottom_right())
            window.draw_line(right_wall_line, fill_color)
        if self.has_top_wall:
            top_wall_line = Line(self.get_top_left(), self.get_top_right())
            window.draw_line(top_wall_line, fill_color)
        if self.has_bottom_wall:
            bottom_wall_line = Line(self.get_bottom_left(), self.get_bottom_right())
            window.draw_line(bottom_wall_line, fill_color)

    # Getter/Setter
    def set_top_left(self, point):
        self.__top_left = point
    def set_top_right(self, point):
        self.__top_right = point
    def set_bottom_left(self, point):
        self.__bottom_left = point
    def set_bottom_right(self, point):
        self.__bottom_right = point
    def get_top_left(self):
        return self.__top_left
    def get_top_right(self):
        return self.__top_right
    def get_bottom_left(self):
        return self.__bottom_left
    def get_bottom_right(self):
        return self.__bottom_right

    def set_win(self, win):
        self.__win = win