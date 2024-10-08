class Maze:
    def __init__(self, maze_name):
        self.path_to_maze_file = f"../mazes/{maze_name}.txt"

        # Read maze file
        with open(self.path_to_maze_file) as f:
            self.maze_raw = self._validate(f.read())

        self.maze_linesplit = self.maze_raw.splitlines()
        self.height = len(self.maze_linesplit)
        self.width = max(len(line) for line in self.maze_linesplit)
        self.start, self.goal, self.walls = self._parse(self.maze_linesplit) 


    def get_neighbors(self, coordinates):
        row, col = coordinates
        possible_neighbors = [
            ('up', (row - 1, col)),
            ('down', (row + 1, col)),
            ('left', (row, col - 1)),
            ('right', (row, col + 1)),
        ]
     
        neighbors = []
        for direction, (r, c) in possible_neighbors:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                neighbors.append((direction, (r, c)))

        return neighbors

    def draw(self, solution=None, explored=None):
        from PIL import Image, ImageDraw

        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        maze = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and (i, j) in explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                ImageDraw.Draw(maze).rectangle(
                    (
                        [
                            (j * cell_size + cell_border, i * cell_size + cell_border),
                            (
                                (j + 1) * cell_size - cell_border,
                                (i + 1) * cell_size - cell_border,
                            ),
                        ]
                    ),
                    fill=fill,
                )

        return maze 

    def print(self, solution=None):
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("■", end=" ")
                elif (i, j) == self.start:
                    print("A", end=" ")
                elif (i, j) == self.goal:
                    print("B", end=" ")
                elif solution is not None and (i, j) in solution:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print()

    def _parse(self, linesplit):
        walls = []
        start = None
        goal = None

        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if linesplit[i][j] == "A":
                        start = (i, j)
                        row.append(False)
                    elif linesplit[i][j] == "B":
                        goal = (i, j)
                        row.append(False)
                    elif linesplit[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            walls.append(row)

        return (start, goal, walls)

    def _validate(self, raw):
        # Validate start and goal
        if raw.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if raw.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        return raw

