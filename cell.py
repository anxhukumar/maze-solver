from graphics import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win != None:
            if self.has_left_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
                
            if self.has_right_wall:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
                
            if self.has_top_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
            else:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
                
            if self.has_bottom_wall:
                self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")
    
    def draw_move(self, to_cell, undo=False):
        middle_point_1 = abs(self.__x1 - self.__x2) // 2
        horizontal_point_1 = self.__x1 + middle_point_1
        vertical_point_1 = self.__y1 + middle_point_1
        point_1 = Point(horizontal_point_1, vertical_point_1)

        middle_point_2 = abs(to_cell.__x1 - to_cell.__x2) // 2
        horizontal_point_2 = to_cell.__x1 + middle_point_2
        vertical_point_2 = to_cell.__y1 + middle_point_2
        point_2 = Point(horizontal_point_2, vertical_point_2)

        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        if self.__win != None:
            self.__win.draw_line(Line(point_1, point_2), fill_color)