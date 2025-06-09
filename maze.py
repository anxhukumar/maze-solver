from cell import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        if seed != None:
            random.seed(seed)
        self.__create_cells()

    def __create_cells(self):
        for c in range(self.num_cols):
            column = []
            for r in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self.__cells.append(column)

        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.__draw_cell(c, r)

        self.__break_entrance_and_exit()

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        if self.win != None:
            cell.draw(x1, y1, x2, y2)
            self.__animate()

    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols-1, self.num_rows-1)
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __break_walls_r(self, col, row):
        self.__cells[col][row].visited = True
        while True:
            visit = []
            
            if col >= 0 and row-1 >=0 and col < len(self.__cells) and row-1 < len(self.__cells[0]):    
                if self.__cells[col][row-1].visited == False:
                    visit.append((col, row-1))
            if col >= 0 and row+1 >=0 and col < len(self.__cells) and row+1 < len(self.__cells[0]):
                if self.__cells[col][row+1].visited == False:
                    visit.append((col, row+1))
            if col-1 >= 0 and row >=0 and col-1 < len(self.__cells) and row < len(self.__cells[0]):
                if self.__cells[col-1][row].visited == False:
                    visit.append((col-1, row))
            if col+1 >= 0 and row >=0 and col+1 < len(self.__cells) and row < len(self.__cells[0]):
                if self.__cells[col+1][row].visited == False:
                    visit.append((col+1, row))
            
            if len(visit) == 0:
                self.__draw_cell(col, row)
                return
            else:
                direction = visit[random.randrange(0,len(visit))]
                next_col, next_row = direction
            
                if next_row < row:  # Moving UP
                    self.__cells[col][row].has_top_wall = False
                    self.__cells[next_col][next_row].has_bottom_wall = False
                elif next_row > row:  # Moving DOWN
                    self.__cells[col][row].has_bottom_wall = False
                    self.__cells[next_col][next_row].has_top_wall = False
                elif next_col < col:  # Moving LEFT
                    self.__cells[col][row].has_left_wall = False
                    self.__cells[next_col][next_row].has_right_wall = False
                else:  # Moving RIGHT
                    self.__cells[col][row].has_right_wall = False
                    self.__cells[next_col][next_row].has_left_wall = False
            self.__break_walls_r(direction[0], direction[1])
    
    def __reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, col, row):
        self.__animate()
        self.__cells[col][row].visited = True
        if col == self.num_cols-1 and row == self.num_rows-1:
            return True
        
        neighbors = []
            
        if col >= 0 and row-1 >=0 and col < len(self.__cells) and row-1 < len(self.__cells[0]):    
            if self.__cells[col][row-1].visited == False:
                neighbors.append((col, row-1))
        if col >= 0 and row+1 >=0 and col < len(self.__cells) and row+1 < len(self.__cells[0]):
            if self.__cells[col][row+1].visited == False:
                neighbors.append((col, row+1))
        if col-1 >= 0 and row >=0 and col-1 < len(self.__cells) and row < len(self.__cells[0]):
            if self.__cells[col-1][row].visited == False:
                neighbors.append((col-1, row))
        if col+1 >= 0 and row >=0 and col+1 < len(self.__cells) and row < len(self.__cells[0]):
            if self.__cells[col+1][row].visited == False:
                neighbors.append((col+1, row))

        for direction in range(len(neighbors)):
            if len(neighbors) > 0:
                i, j = neighbors[direction]
                if j < row and self.__cells[col][row].has_top_wall == False and self.__cells[i][j].has_bottom_wall == False:
                    self.__cells[col][row].draw_move(self.__cells[i][j])
                    output = self._solve_r(i, j)
                    if output == True:
                        return True
                    self.__cells[col][row].draw_move(self.__cells[i][j], True)
                elif j > row and self.__cells[col][row].has_bottom_wall == False and self.__cells[i][j].has_top_wall == False:  
                    self.__cells[col][row].draw_move(self.__cells[i][j])
                    output = self._solve_r(i, j)
                    if output == True:
                        return True
                    self.__cells[col][row].draw_move(self.__cells[i][j], True)
                elif i < col and self.__cells[col][row].has_left_wall == False and self.__cells[i][j].has_right_wall == False:
                    self.__cells[col][row].draw_move(self.__cells[i][j])
                    output = self._solve_r(i, j)
                    if output == True:
                        return True
                    self.__cells[col][row].draw_move(self.__cells[i][j], True)
                elif i > col and self.__cells[col][row].has_right_wall == False and self.__cells[i][j].has_left_wall == False:
                    self.__cells[col][row].draw_move(self.__cells[i][j])
                    output = self._solve_r(i, j)
                    if output == True:
                        return True
                    self.__cells[col][row].draw_move(self.__cells[i][j], True)
        return False