import sys
from time import sleep

import json

from src.dfs_maze import DfsMaze
from src.mst_maze import MstMaze


class App:
    def __init__(self):
        sys.setrecursionlimit(5000)

        print()
        size = 0
        while size == 0:
            try:
                size = int(input("What maze size do you want? [an integer from [2:100]] "))
                if not 2 <= size <= 100:
                    size = 0
                    raise ValueError
            except ValueError:
                print("INCORRECT: input an integer from [2:100]", file=sys.stderr, flush=True)
                sleep(1)

        print()
        generation_method = ""
        while generation_method == "":
            try:
                generation_method = input("Which method to use: "
                                          "Depth First Search or Minimum Spanning Tree? [DFS/MST] ")
                if generation_method.upper() == "DFS":
                    self.maze = DfsMaze(size)
                elif generation_method.upper() == "MST":
                    self.maze = MstMaze(size)
                else:
                    generation_method = ""
                    raise ValueError
            except ValueError:
                print("INCORRECT: input a string from {\"DFS\", \"MST\"}", file=sys.stderr, flush=True)
                sleep(1)

    def get_maze_image(self):
        """
        Prints the maze.
        """

        print("\n" + self.maze.get_image() + "\n")
        sleep(2)

    def get_solution_image(self):
        """
        Prints a solution of the maze.
        """

        get_solution = ""
        while get_solution == "":
            try:
                get_solution = input("Do you want to get a solution? [Y/N] ")
                if get_solution.upper() == "Y":
                    print("\n" + self.maze.get_solution() + "\n")
                elif get_solution.upper() != "N":
                    get_solution = ""
                    raise ValueError
            except ValueError:
                print("INCORRECT: input a string from {\"Y\", \"N\"}", file=sys.stderr, flush=True)
                sleep(1)

    def save_maze_image(self):
        """
        Saves the maze in the "database".
        """

        print()
        save_maze = ""
        while save_maze == "":
            try:
                save_maze = input("Do you want to save the maze? [Y/N] ")
                if save_maze.upper() == "Y":
                    codename = input("Enter a codename for the maze: ")
                    with open("data.json", "r") as file:
                        data = json.load(file)
                        data[codename] = (self.maze.get_image(), self.maze.get_solution())
                    with open("data.json", "w") as file:
                        json.dump(data, file)
                elif save_maze.upper() != "N":
                    save_maze = ""
                    raise ValueError
            except ValueError:
                print("INCORRECT: input a string from {\"Y\", \"N\"}", file=sys.stderr, flush=True)
                sleep(1)

    def get_saved_maze_image(self):
        """
        Prints a maze from the "database".
        """

        print()
        save_maze = ""
        while save_maze == "":
            try:
                save_maze = input("Do you want to get a saved maze? [Y/N] ")
                if save_maze.upper() == "Y":
                    codename = input("Enter a codename for a saved maze: ")
                    with open("data.json", "r") as file:
                        data = json.load(file)
                        print(data[codename][0])
                elif save_maze.upper() != "N":
                    save_maze = ""
                    raise ValueError
            except ValueError:
                print("INCORRECT: input a string from {\"Y\", \"N\"}", file=sys.stderr, flush=True)
                sleep(1)

    def get_saved_solution_image(self):
        """
        Prints a solution of a maze from the "database".
        """

        print()
        save_maze = ""
        while save_maze == "":
            try:
                save_maze = input("Do you want to get a solution of a saved maze? [Y/N] ")
                if save_maze.upper() == "Y":
                    codename = input("Enter a codename for a saved maze: ")
                    with open("data.json", "r") as file:
                        data = json.load(file)
                        print(data[codename][1])
                elif save_maze.upper() != "N":
                    save_maze = ""
                    raise ValueError
            except ValueError:
                print("INCORRECT: input a string from {\"Y\", \"N\"}", file=sys.stderr, flush=True)
                sleep(1)


if __name__ == "__main__":
    print("Hello! This is a Maze Generator.")
    app = App()
    app.get_maze_image()
    app.get_solution_image()
    app.save_maze_image()
    app.get_saved_maze_image()
    app.get_saved_solution_image()
    print("\nBye!")
