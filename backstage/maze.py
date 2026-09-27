wall = 1
path = 0

# Phase 1: Solid baseline
down = (-1, 0)
up =   (1, 0)
left = (0, -1)
right = (0, 1)
# Phase 2: Add these whenever you are ready
# DIRECTIONS += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

class maze:
    
    def __init__(self, row: int , col: int):
        self.row = row
        self.col = col
        self.maze = [[wall for _ in range(col)] for _ in range(row)]
        self.start = (0, 0)
        self.start = path
        self.end = (row - 1, col - 1)
        self.generate_maze()

    def generate_maze(self):
        current_state = self.start 


        trace = [current_state]
        visited = {current_state}

        while True:
            direction = self.randomly_select_direction(current_state) 

            if direction is None:
                return("in maze.py, generate_maze: No valid direction found. Maze generation may be complete or stuck.")
            elif direction[0] == "outline" or direction[0] == "path":
                #step back to the previous state and try a different direction
                #mark this state as visited to avoid going back to it(it is a path so it won't be visited again)
                continue 

            new_state = (current_state[0] + direction[1][0], current_state[1] + direction[1][1])
            print(f"Moving from {current_state} to {new_state} in direction {direction[1]}")
            new_state = path

            if direction[0] == "end" :
                print ("reached the end")
            else :
                current_state = new_state
                continue



    def randomly_select_direction(self, current_state: tuple[int, int]) ->  list[str, tuple[int, int]]:
        import random
        directions = [down, up, left, right]
        random.shuffle(directions)
        for direction in directions:
            new_pos = (current_state[0] + direction[0], current_state[1] + direction[1])
            return [self.get_state(new_pos), direction]
        return None
        

    def get_state(self, pos: tuple[int, int]) -> str:
        r, c = pos
        if not (0 <= r < self.row and 0 <= c < self.col):
            return "out_of_bounds"
        if pos == self.start:
            return "start"
        if pos == self.end:
            return "end"
        if r == 0 or r == self.row - 1 or c == 0 or c == self.col - 1:
            return "outline"
        if self.maze[r][c] == wall:
            return "wall"
        return "path"

    def move(self, current_state: tuple[int, int], direction: tuple[int, int]) -> tuple[tuple[int, int], str]:
        new_pos = (current_state[0] + direction[0], current_state[1] + direction[1])
        return new_pos, self.get_state(new_pos)

    def move_down(self, current_state: tuple[int, int]) -> tuple[tuple[int, int], str]:
        return self.move(current_state, down)

    def move_up(self, current_state: tuple[int, int]) -> tuple[tuple[int, int], str]:
        return self.move(current_state, up)

    def move_left(self, current_state: tuple[int, int]) -> tuple[tuple[int, int], str]:
        return self.move(current_state, left)

    def move_right(self, current_state: tuple[int, int]) -> tuple[tuple[int, int], str]:
        return self.move(current_state, right)

    def watch_neighbors(self, current_state: tuple[int, int]) -> dict[str, tuple[tuple[int, int], str]]:
        return {
            "down": self.move_down(current_state),
            "up": self.move_up(current_state),
            "left": self.move_left(current_state),
            "right": self.move_right(current_state),
        }