from src.gui.gui import Window
from src.models.maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(50, 50,10,14, 0, 50,False)
    window.draw_maze(maze, "cyan")
    window.wait_for_close()

if __name__ == '__main__':
    main()


