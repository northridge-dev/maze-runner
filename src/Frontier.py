from abc import ABC, abstractmethod

class Frontier(ABC):
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    @abstractmethod
    def remove(self):
        """Remove and return a node from the frontier."""
        pass


class DepthFirstFrontier(Frontier):
    """Use a stack to implement a depth-first search (DPS)"""

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class BreadthFirstFrontier(Frontier):
    """Use a queue to implement a breadth-first search (BFS)""" 

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
