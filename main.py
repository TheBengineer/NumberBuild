from objects import *

goal = 13
possible_numbers = [1, 2]
max_number = max(possible_numbers)

mul_lookup = {}
paths = []


def search_add(current, goal):
    if current + max_number >= goal:
        diff = goal - current
        if diff in possible_numbers:
            return Add(current, diff)
        else:
            return None
    else:
        return current


def search_sub(current, goal):
    if current - max_number <= goal:
        diff = goal + current
        if diff in possible_numbers:
            return Sub(current, diff)
        else:
            return None
    else:
        return current


f = search_add(0, goal)
print(f)
