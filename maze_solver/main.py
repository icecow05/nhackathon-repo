import queue
import time
def read_maze(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    mazes = {}
    current_maze = None
    current_grid = []
    start_rows = {}
    maze_indicators = []
    end_rows = {}
    for line in lines:
        line = line.strip()

        if line:
            if line.isalpha():
                current_maze = line
                current_grid = []
                maze_indicators.append(current_maze)
                start_rows[current_maze] = []
                end_rows[current_maze] = []
                index = 0
            else:
                row = list(line.split())#.split()
                current_grid.append(row)
                index += 1
                if "S" in row:
                    start_rows[current_maze].append(index-1)
                if "G" in row:
                    end_rows[current_maze].append(index-1)
                    
        if current_maze and current_grid:
            mazes[current_maze] = current_grid
    return mazes, start_rows, end_rows, maze_indicators


# Bemeneti fájl neve
filename = 'maze_solver/input.txt'

# Labirintusok beolvasása
mazes, start_row, end_row, maze_indicators = read_maze(filename)
#print(mazes["A"])
# Az 'A' labirintus kiíratása példaként

#def display_maze(maze):
#    for row in maze:
#        print(''.join(row))
#    print()

#print("A")
#display_maze(mazes['A'])
#display_maze(mazes['B'])
#display_maze(mazes['C'])
#print(start_row[maze_indicators[mazecounter][0]], end_row)
def printMaze(maze, mazecounter, path=""):
    #print(maze[start_row["A"][0]])
    start = None
    for x, pos in enumerate(maze[start_row[maze_indicators[mazecounter]][0]]): # "A" helyett "B C D" is lehet és 0 helyett n(mazes) darabú szám
        if pos == "S":
            start = x
    i = start
    j = start_row[maze_indicators[mazecounter]][0]
    pos = set()
    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("* ", end="")
            else:
                print(col + " ", end="")
        print()

def valid(maze, moves, start_row):
    for x, pos in enumerate(maze[start_row[maze_indicators[mazecounter]][0]]):
        if pos == "S":
            start = x
    i = start
    j = start_row[maze_indicators[mazecounter]][0]
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    
    return True
def findEnd(maze, moves, start_row):
    for x, pos in enumerate(maze[start_row[maze_indicators[mazecounter]][0]]):
        if pos == "S":
            start = x
            i = start 
    j = start_row[maze_indicators[mazecounter]][0]
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
    if maze[j][i] == "G":
        #print(maze)
        print(f"S {' '.join(moves)} G\n")
        #printMaze(maze, moves)
        return True
    
    return False

#print(maze[start_row["A"][0]])
mazecounter = -1 # -1 volt
#print(start_row[maze_indicators[mazecounter]][0])
#print(maze_indicators)
#print(len(mazes)-1)
#print(start_row)
#print(maze_indicators[mazecounter])
#print(maze_indicators[mazecounter])
for i in range(len(mazes)):
   mazecounter += 1
   maze = mazes[maze_indicators[mazecounter]]
   #print(maze[start_row[maze_indicators[mazecounter]][mazecounter]])
   #print(maze[start_row[maze_indicators[mazecounter]][0]])
   print(maze_indicators[mazecounter])
   #print(maze_indicators[mazecounter]
   nums = queue.Queue()
   nums.put("")
   add = ""
   #print(mazes[maze_indicators[mazecounter]])
   while not findEnd(maze, add, start_row): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put, start_row):
            if len(put) < 3:
                nums.put(put)
            else:
                if put[-1] == "L" and put[-2] != "R" or put[-1] == "R" and put[-2] != "L" or put[-1] == "U" and put[-2] != "D" or put[-1] == "D" and put[-2] != "U":
                    nums.put(put)
                    #printMaze(maze, mazecounter)
