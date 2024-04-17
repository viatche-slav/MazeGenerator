from random import randint
from copy import deepcopy


class Maze:
    def __init__(self, size: int):
        self.size = size
        self.graph = [list() for _ in range(size ** 2)]
        self.used = [False for _ in range(size ** 2)]
        self.grid = [["+" if column % 2 == 0 else " ——— " for column in range(2 * self.size + 1)]
                     if row % 2 == 0 else
                     ["|" if column % 2 == 0 else "     " for column in range(2 * self.size + 1)]
                     for row in range(2 * self.size + 1)]
        self.start, self.finish = randint(0, self.size - 1), randint(0, self.size - 1)
        self.parent = [-1 for _ in range(size ** 2)]

    def get_image(self):
        """
        A method that converts graph into an image of a maze.

        :return: A string with a maze.
        """

        self.used = [False for _ in range(self.size ** 2)]
        self.make_maze(0)
        self.grid[0][2 * self.start + 1] = "     "
        self.grid[2 * self.size][2 * self.finish + 1] = "     "
        return ' ' * (6 * self.start + 3) + "↓\n" + \
            '\n'.join(map(''.join, self.grid)) + \
            "\n" + ' ' * (6 * self.finish + 3) + "↓"

    def make_maze(self, vertex: int):
        """
        An auxiliary (recursive) method to convert a graph into an image.

        :param vertex: The vertex that is being processed in this iteration.
        """

        self.used[vertex] = True
        for next_vertex in self.graph[vertex]:
            if self.used[next_vertex]:
                continue
            if next_vertex == vertex - self.size:
                self.grid[2 * (vertex // self.size)][2 * (vertex % self.size) + 1] = "     "
            elif next_vertex == vertex - 1:
                self.grid[2 * (vertex // self.size) + 1][2 * (vertex % self.size)] = " "
            elif next_vertex == vertex + 1:
                self.grid[2 * (vertex // self.size) + 1][2 * (vertex % self.size) + 2] = " "
            elif next_vertex == vertex + self.size:
                self.grid[2 * (vertex // self.size) + 2][2 * (vertex % self.size) + 1] = "     "
            self.make_maze(next_vertex)

    def get_neighbors(self, vertex: int):
        """
        An auxiliary method to get neighbors of a cell (vertex) in a grid (graph).

        :param vertex: A cell.
        :return: A list of neighbors of a cell.
        """

        neighbors = list()
        if vertex >= self.size:
            neighbors.append(vertex - self.size)
        if vertex % self.size > 0:
            neighbors.append(vertex - 1)
        if vertex % self.size < self.size - 1:
            neighbors.append(vertex + 1)
        if vertex < self.size ** 2 - self.size:
            neighbors.append(vertex + self.size)
        return neighbors

    def get_solution(self):
        """
        A method that solves the maze.

        :return: A string with solved maze.
        """

        grid = deepcopy(self.grid)
        self.used = [False for _ in range(self.size ** 2)]
        self.dfs(self.start)
        vertex = self.size ** 2 + self.finish
        previous_vertex = vertex - self.size
        while previous_vertex != -1:
            if vertex == previous_vertex - self.size:
                grid[2 * (previous_vertex // self.size) + 1][2 * (previous_vertex % self.size) + 1] = "  ↑  "
            elif vertex == previous_vertex + self.size:
                grid[2 * (previous_vertex // self.size) + 1][2 * (previous_vertex % self.size) + 1] = "  ↓  "
            elif vertex == previous_vertex - 1:
                grid[2 * (previous_vertex // self.size) + 1][2 * (previous_vertex % self.size) + 1] = "  ←  "
            elif vertex == previous_vertex + 1:
                grid[2 * (previous_vertex // self.size) + 1][2 * (previous_vertex % self.size) + 1] = "  →  "
            vertex = previous_vertex
            previous_vertex = self.parent[vertex]
        return ' ' * (6 * self.start + 3) + "↓\n" + \
            '\n'.join(map(''.join, grid)) + \
            "\n" + ' ' * (6 * self.finish + 3) + "↓"

    def dfs(self, vertex: int):
        """
        An auxiliary (recursive) method to solve the maze.

        :param vertex: The vertex that is being processed in this iteration.
        """

        self.used[vertex] = True
        for next_vertex in self.graph[vertex]:
            if not self.used[next_vertex]:
                self.parent[next_vertex] = vertex
                self.dfs(next_vertex)
