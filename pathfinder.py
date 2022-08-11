import curses
from curses import wrapper
import queue
import time


user_input = input('Insert Desired Maze#(1, 2, 3): ')
if user_input == '1':
        maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "O", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["X", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]
elif user_input == '2':
    maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", "#", "#", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", " ", " ", " ", "X"],
    ["#", " ", "#", " ", " ", " ", " ", "#", "#", "#", " ", "#"],
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]  
    ]

elif user_input == '3':
    maze = [
    ["#", "X", "#", "#", "#"],
    ["#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", " ", "#", "#"],
    ["#", " ", " ", "#", "#"],
    ["#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "O"],
    ["#", "#", "#", "#", "#"]
    ]

else:
    print('Invalid User Input - Default Maze #1 Selected.')
    time.sleep(2)
    maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "O", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["X", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                 stdscr.addstr(i * 2, j * 3, "X", RED)
            else:
                stdscr.addstr(i * 2, j * 3, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
        
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            r, c = neighbor
            if maze[r][c] == '#':
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

        
def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # DOWN
        neighbors.append((row + 1, col))
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))

    return neighbors
    

# Standard Output Screen
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)
    find_path(maze, stdscr)
    stdscr.getch()
    exit()

wrapper(main)