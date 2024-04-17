from random import shuffle

from src.maze import Maze


class DfsMaze(Maze):
    def __init__(self, size: int):
        super().__init__(size)
        self.randomized_dfs(0)

    def randomized_dfs(self, vertex: int):
        """
        The main method of the class. Creates a graph for the maze using randomized Depth First Search.
        """

        self.used[vertex] = True
        randomly_ordered_neighbors = self.get_neighbors(vertex)
        shuffle(randomly_ordered_neighbors)
        for next_vertex in randomly_ordered_neighbors:
            if next_vertex in range(self.size ** 2) and not self.used[next_vertex]:
                self.graph[vertex].append(next_vertex)
                self.graph[next_vertex].append(vertex)
                self.randomized_dfs(next_vertex)
