import heapq

def read_maze(filename):
    # Read maze from the input file
    with open(filename, 'r') as file:
        lines = file.readlines()

    mazes = {}
    start_rows = {}
    end_rows = {}
    maze_indicators = []

    current_maze = None
    current_grid = []

    # Parse each line of the input file
    for line in lines:
        line = line.strip()

        if line:
            # Identify maze indicators (alphabetic lines)
            if line.isalpha():
                current_maze = line
                current_grid = []
                maze_indicators.append(current_maze)
                start_rows[current_maze] = []
                end_rows[current_maze] = []
                index = 0
            else:
                # Parse maze rows and identify start ("S") and goal ("G") positions
                row = list(line.split())
                current_grid.append(row)
                index += 1
                if "S" in row:
                    start_rows[current_maze].append(index - 1)
                if "G" in row:
                    end_rows[current_maze].append(index - 1)

        if current_maze and current_grid:
            mazes[current_maze] = current_grid

    return mazes, start_rows, end_rows, maze_indicators

def dijkstra(maze, start, end):
    # Initialize matrix to store distances from the start to each cell
    rows, cols = len(maze), len(maze[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    # Priority queue storing nodes with distance and coordinates
    heap = [(0, start)]

    # Main loop for exploring nodes
    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Check if the current node is the goal
        if current_node == end:
            return distances[end[0]][end[1]]

        # Explore possible moves: right, down, left, up
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_node = (current_node[0] + move[0], current_node[1] + move[1])

            # Check if the new node is within maze bounds and not blocked
            if 0 <= new_node[0] < rows and 0 <= new_node[1] < cols and maze[new_node[0]][new_node[1]] != "#":
                new_dist = current_dist + 1

                # Update distance for the new node
                if new_dist < distances[new_node[0]][new_node[1]]:
                    distances[new_node[0]][new_node[1]] = new_dist
                    heapq.heappush(heap, (new_dist, new_node))

    # If the goal is not reached, return infinity
    return float('inf')

def find_shortest_path(maze, start, end):
    # Initialize matrix to store distances from the start to each cell
    rows, cols = len(maze), len(maze[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    # Priority queue storing nodes with distance and path
    heap = [(0, start, [])]

    # Main loop for exploring nodes
    while heap:
        current_dist, current_node, current_path = heapq.heappop(heap)

        # Goal check
        if current_node == end:
            return current_path

        # Explore possible moves: right, down, left, up
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_node = (current_node[0] + move[0], current_node[1] + move[1])

            # Check if the new node is within maze bounds and not blocked
            if 0 <= new_node[0] < rows and 0 <= new_node[1] < cols and maze[new_node[0]][new_node[1]] != "#":
                new_dist = current_dist + 1

                # Update distance and path for the new node
                if new_dist < distances[new_node[0]][new_node[1]]:
                    distances[new_node[0]][new_node[1]] = new_dist
                    new_path = current_path + [move]

                    # Add new nodes to the heap for further exploration
                    heapq.heappush(heap, (new_dist, new_node, new_path))

    # If the goal is not reached, return an empty path
    return []


def print_solution(maze, start, end, path):
    # Print the maze with the marked shortest path and print the shortest path
    for move in path:
        start = (start[0] + move[0], start[1] + move[1])
        maze[start[0]][start[1]] = '*'

    for row in maze:
        print(' '.join(row))
    print()

# Input file name
filename = './input.txt'

# Read mazes from the input file
mazes, start_rows, end_rows, maze_indicators = read_maze(filename)

# Iterate through mazes
for maze_indicator in maze_indicators:
    maze = mazes[maze_indicator]
    start_row = start_rows[maze_indicator][0]
    end_row = end_rows[maze_indicator][0]

    start = (start_row, maze[start_row].index("S"))
    end = (end_row, maze[end_row].index("G"))

    # Find the shortest path for each maze
    shortest_path = find_shortest_path(maze, start, end)
    
    if shortest_path:
        # Print maze indicator and the shortest path
        print(maze_indicator)
        print(f"S {' '.join(['L' if move == (0, -1) else 'R' if move == (0, 1) else 'U' if move == (-1, 0) else 'D' for move in shortest_path])} G")
        #Uncomment the line below if you want to print out the maze with the shortest path marked :)
        #print_solution(maze, start, end, shortest_path)
    else:
        print(f"No solution found for maze {maze_indicator}")