from graphics import Window
from maze import Maze

def main():
    win = Window(1000, 1000)
    
    # Maze(x1, y1, rows, columns, cell_size_x, cell_size_y, window, seed)
    # Set the seed to a fixed integer if you want the same maze everytime and 'None' for randomized maze which is the default.
    maze = Maze(120,100,13,13,60,60,win)
    maze.solve()
    win.wait_for_close()

main()