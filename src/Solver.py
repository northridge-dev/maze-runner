from Frontier import BreadthFirstFrontier, DepthFirstFrontier
from Maze import Maze


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class MazeSolver:
    def __init__(self, maze, strategy="dfs"):
        self.maze = maze
        self.strategy = strategy
        self.solution, self.actions = self._solve() 

    def change_strategy(self, strategy):
        if strategy != "dfs" and strategy != "bfs":
            raise Exception("dfs and bfs are only valid strategies")

        if self.strategy != strategy:
            self.strategy = strategy
            self.solution, self.action = self._solve()


    def _solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.maze.start, parent=None, action=None)
        frontier = DepthFirstFrontier() if self.strategy == "dfs" else BreadthFirstFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.maze.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                return cells, actions

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.maze.get_neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
