#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Solver for the Genshin Impact Pillar Puzzle

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


def find_pillars(state):
    """Generator to work out which pillars need to be flipped.

    This checks each pillar and if it's off, it yields that pillar and the two either side of it.

    :param state: Current state of the puzzle
    :return:  The positions of the pillars to be flipped from on to off and vise versa.
    """
    last = len(state) - 1
    for i, pillar in enumerate(state):
        if i == 0 and pillar == 0:  # if the first pillar is off, flip it and the ones either side
            yield [last, 0, 1]
            continue
        if i == last and pillar == 0:  # if the last pillar is off, flip it and the ones either side
            yield [last - 1, last, 0]
            continue
        elif pillar == 0:  # if a middle pillar is off, flip it and the ones either side
            yield [i - 1, i, i + 1]


def move(state):
    """Find the next state to move to based on the current state

    :param state: Array containing the current status of all pillars in the puzzle
    :return:      The next state of the puzzle, where one pillar has been turned on (and flipped the others).
    """
    for pillars in find_pillars(state):  # function returns a list of pillars to be flipped
        initial_state = copy.deepcopy(state)
        for pillar in pillars:
            state[pillar] = 1 if state[pillar] == 0 else 0  # if this pillar is off, turn it on, otherwise turn it off
        yield [pillars[1], state]  # send back the pillar activated and the new state
        state = initial_state


def dls_rec(path, limit):
    """Depth Limited Search called recursively to a given depth.

    :param path:  List of all states from the initial state to the current state.
    :param limit: Depth to iterate down to.
    :return:      List of states from initial to goal and a flag for if there are any remaining nodes.
    """
    if limit == 0:
        if is_goal(path[-1]):  # pass in the last state in the path
            return [path, False, []]
        else:
            return [None, True, None]  # we didn't find a solution yet but there are child nodes to discover
    else:
        cutoff = False  # this is true if there are child nodes but we can't reach them at the current depth
        cur_state = copy.deepcopy(path[-1])

        for pillar, nextState in move(cur_state):
            if nextState not in path:
                next_path = path + [nextState]  # add the new state to the list of states generated.
                returned_path, remaining_moves, pillars = dls_rec(next_path, limit - 1)

                if returned_path is not None:
                    pillars.insert(0, pillar + 1)
                    return [returned_path, False, pillars]  # unwinding recursion as solution was found
                if remaining_moves:
                    cutoff = True  # solution not found but there are child nodes, increase limit

        return [None, cutoff, None]  # we didn't find a solution here, report if there are child nodes left


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
        path, remaining_moves, pillars = dls_rec([root], limit)

        if path is not None:  # we found the path, send back the moves and calls
            return pillars
        elif not remaining_moves:  # no path exists to the goal
            return None
        limit += 1  # if there are child nodes still to expand, go one level deeper


def validate_input(state):
    try:
        int(state)
    except ValueError:
        print("Please only enter digits.")
        return None

    root = []
    for digit in state:
        if (digit != '0') and (digit != '1'):
            print("Please enter your puzzle state using only numbers 0 and 1. i.e. 11010")
            return None
        root.append(int(digit))

    if len(root) < 4:
        print("Minimum number of pillars is 5.")
        return None

    if len(root) % 2 == 0:
        print("Only puzzles with an odd number of pillars are solvable.")
        return None

    return root


def print_solution(solution):
    for pillar in solution:
        print("Activate pillar", pillar)
    print()


def main():
    """Main function.

    Gives test states with the state representation [n1, n2, ..., nx] where n is the status of a pillar where 1 is
    on and 0 is off, and x is the total number of pillars in the puzzle. Numbers are in the order of the first pillar
    in front of the character going round clockwise to one before the first one. These states are passed into the IDS
    algorithm to be processed.
    """
    print("Starting from the pillar in front of you and working clockwise from there, enter a 1 for\n"
          "pillars that are on and 0 for those that are off. For example \"10001\" if the pillar in front\n"
          "of you and the pillar to the right of that are on.")
    while True:
        state = input("Please enter the current state of your puzzle:")
        # state = [1, 1, 0, 1, 0]  # for testing, comment out the line above and uncomment this line.
        # test answer: [1, 1, 0, 1, 0] -> [1, 0, 1, 0, 0] -> [0, 1, 0, 0, 0] -> [0, 0, 1, 1, 0] -> [1, 1, 1, 1, 1]
        root = validate_input(state)
        if root is None:
            continue
        break

    print("To get from", root, "to a complete puzzle:")
    solution = iddfs_rec(root)

    if solution is None:
        print("No Solution")
    else:
        print_solution(solution)


main()
