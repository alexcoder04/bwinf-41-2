#!/usr/bin/env python3

import random
import sys

from lib import get_datapoints, dist, angle
from visualize import visualize

def closest_point_with_angle(points: list[tuple[float]], prev_point: int, curr_point: int, visited: set[int], unvisited: set[int], min_angle: float) -> int:
    """Finds the closest point that satisfies the minimum angle condition"""
    closest = None
    min_dist = float("inf")
    # iterate over all other points
    for point_index in unvisited:
        # calculate distance
        d = dist(points[curr_point], points[point_index])
        # calculate angle (no prev point -> no angle yet -> 0)
        if prev_point is None:
            a = 0
        else:
            a = angle(points[prev_point], points[curr_point], points[point_index])
        # too large angle -> we don't care
        if a > 90:
            continue
        # distance less?
        if d < min_dist:
            min_dist = d
            closest = point_index
    return closest

def find_route(points: list[tuple[float]]) -> list[tuple[float]]:
    # assume first point to be the first in our route
    route = [0] # route is a list of indices of points
    unvisited = set([i for i in range(1, len(points))]) # unvisited is a set of indices of points
    # run as long as we still have unvisited points
    while unvisited:
        # find the closest point
        if len(route) < 2:
            closest = closest_point_with_angle(points, None, route[-1], set(route), unvisited, 90)
        else:
            closest = closest_point_with_angle(points, route[-2], route[-1], set(route), unvisited, 90)

        # current point leads to dead end
        if closest is None:
            return None

        # add to route
        route.append(closest)
        unvisited.remove(closest)
        dead_ends = set([])

    return route

def run(command: str, arg: str):
    if command == "solve":
        data = get_datapoints(arg)
        print(f"Solving example {arg}, points: {data}")
        res = find_route(data)
        if res is None:
            print("No solution found")
            return
        print(f"Solution: {res}")
        return
    
    if command == "visualize":
        data = get_datapoints(arg)
        print(f"Solving example {arg}, points: {data}")
        res = find_route(data)
        if res is None:
            print("No solution found")
            return
        print(f"Solution: {res}")
        print("Starting GUI for visualization...")
        visualize(data, res)
        return
    
    print(f"""Usage: {sys.argv[0]} [command] [argument]
    commands:
        help:       print this help
        solve:      solve example (argument is path to example file)
        visualize:  solve example and show the solution visually (argument is path to example)""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        command = "help"
        arg = ""
    elif len(sys.argv) < 3:
        command = sys.argv[1]
        arg = "../task1/data/wenigerkrumm1.txt"
    else:
        command = sys.argv[1]
        arg = sys.argv[2]
    run(command, arg)

