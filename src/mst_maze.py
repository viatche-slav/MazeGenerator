from random import randint

from src.maze import Maze


class MstMaze(Maze):
    def __init__(self, size: int):
        super().__init__(size)
        self.mst()

    def mst(self):
        """
        The main method of the class. Creates a graph for the maze using Minimum Spanning Tree.
        """

        weights = [dict() for _ in range(self.size ** 2)]
        vertex = 0
        while vertex < self.size ** 2:
            for neighbor in [vertex - self.size, vertex - 1, vertex + 1, vertex + self.size]:
                if neighbor in range(self.size ** 2):
                    weight = randint(1, 2 * self.size ** 2)
                    weights[vertex][neighbor] = weight
                    weights[neighbor][vertex] = weight
            vertex += 2
            if self.size % 2 == 0:
                if vertex % self.size == 0:
                    vertex += 1
                elif vertex % self.size == 1:
                    vertex -= 1
        self.used[0] = True
        splitting_edges = [(0, 1), (0, self.size)]
        while not all(self.used):
            start, end = min(splitting_edges, key=lambda edge: weights[edge[0]][edge[1]])
            self.graph[start].append(end)
            self.graph[end].append(start)
            self.used[end] = True
            for neighbor in self.get_neighbors(end):
                if neighbor in range(self.size ** 2):
                    if self.used[neighbor]:
                        splitting_edges.remove((neighbor, end))
                    else:
                        splitting_edges.append((end, neighbor))
