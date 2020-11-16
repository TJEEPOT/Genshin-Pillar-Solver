#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Solution of the Genshin Impact Pillar Puzzle

File    : solver.py
Date    : Monday 16 November 2020
Desc.   : An algorithm which solves the Genshin Impact Pillar Puzzle by utilising an Iterative Deepening DFS.
History : 16/11/2020 - v1.0 - Create basic project file.

"""
import copy


__author__ = "Martin Siddons"
__copyright__ = "Copyright 2020, Martin Siddons"
__credits__ = ["Martin Siddons"]
__license__ = "MIT"
__version__ = "1.0"
__email__ = "tjeepot@gmail.com"
__status__ = "Development"  # or "Production"


def is_goal(state):
    """Check if the solution state has been found, where all pillars are on.

    :param state: Current state of the puzzle
    :return:      Boolean, true if the solution has been found.
    """
    for pillar in state:
        if pillar == 0:
            return False
    return True


# def flip_pillars(i):
#     """Generator to change the position of the blank tile.
#
#     The movement of the blank tile is dependant on which tiles surround it.
#
#     :param i: The row of the blank tile.
#     :param j: The column of the blank tile.
#     :param n: The square root of the puzzle area (i.e. for a 4x4 puzzle, n = 4)
#     :return:  The row and column of the tile to switch the blank with.
#     """
#     if i + 1 < n:   # check for a tile to the bottom
#         yield (i + 1, j)
#     if i - 1 >= 0:  # check for a tile to the top
#         yield (i - 1, j)
#     if j + 1 < n:   # check for a tile to the right
#         yield (i, j + 1)
#     if j - 1 >= 0:  # check for a tile to the left
#         yield (i, j - 1)


def move(state):
    """Find the next state to move to based on the current state

    :param state: Array containing the current status of all pillars in the puzzle
    :return:      The next state of the puzzle, where one pillar has been turned on (and flipped the others).
    """
    # for pillar in state():
    #     if pillar == 0:
    return state


def dls_rec(path, limit):
    """Depth Limited Search called recursively to a given depth.

    :param path:  List of all states from the initial state to the current state.
    :param limit: Depth to iterate down to.
    :return:      List of states from initial to goal and a flag for if there are any remaining nodes.
    """
    if limit == 0:
        if is_goal(path[-1]):  # pass in the last state in the path
            return [path, False]
        else:
            return [None, True]  # we didn't find a solution yet but there are child nodes to discover
    else:
        cutoff = False  # this is true if there are child nodes but we can't reach them at the current depth
        cur_state = copy.deepcopy(path[-1])
        for nextState in move(cur_state):
            if nextState not in path:
                next_path = path + [nextState]  # add the new state to the list of states generated.
                path, remaining_moves = dls_rec(next_path, limit - 1)

                if path is not None:
                    return [path, False]  # unwinding recursion as solution was found
                if remaining_moves:
                    cutoff = True  # solution not found but there are child nodes, increase limit

        return [None, cutoff]  # we didn't find a solution here, report if there are child nodes left


def iddfs_rec(root):
    """Depth First Search of given state with Iterative Deepening.

    Sets up iterative deepening on the depth limited search algorithm to discover the shortest path to the solution
    without exceeding the size of the recursive stack.

    :param root: Initial state of puzzle to solve.
    :return:     List containing the number of moves taken to solve and the total number of calls made to the move
    procedure.
    """
    limit = 0

    while True:
        path, remaining_moves = dls_rec(root, limit)

        if path is not None:  # we found the path, send back the moves and calls
            return [path]
        elif not remaining_moves:  # no path exists to the goal
            return None
        limit += 1  # if there are child nodes still to expand, go one level deeper


def main():
    """Main function.

    Gives a test state with the state representation [n1, n2, ..., nx] where n is the status of a pillar where 1 is
    on and 0 is off, and x is the total number of pillars in the puzzle. These states are then passed into the IDS
    algorithm to be processed.
    """
    states_list = [[1, 1, 0, 1, 0], [1, 0, 0, 1, 0]]

    for i, root in enumerate(states_list):
        print("Initial State:", root)
        solution = iddfs_rec(root)

        if solution is None:
            print("No Solution")
        else:
            for state in solution:
                print(state)
            print()


main()
