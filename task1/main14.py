#!/usr/bin/env python3

import random
import sys

from lib import get_datapoints2, dist, angle, route_length

def closest_point_with_angle(points: list[tuple[float]], dead_ends: set[int], prev_point: int, curr_point: int, visited: set[int], unvisited: set[int], min_angle: float) -> int:
    closest = None
    min_dist = float("inf")
    # iterate over all other points
    for point_index in unvisited:
        # don't care if we know this is a dead end
        if point_index in dead_ends:
            continue
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
    route = [0] # indices only
    unvisited = set([i for i in range(1, len(points))]) # indices only
    dead_ends = set([]) # indices
    # run as long as we still have unvisited points
    while unvisited:
        # find the closest point
        if len(route) < 2:
            closest = closest_point_with_angle(points, dead_ends, None, route[-1], set(route), unvisited, 90)
        else:
            closest = closest_point_with_angle(points, dead_ends, route[-2], route[-1], set(route), unvisited, 90)

        # current point leads to dead end
        if closest is None:
            return None

        # add to route
        route.append(closest)
        unvisited.remove(closest)
        dead_ends = set([])

    return route

if __name__ == "__main__":
    if len(sys.argv) > 1:
        example = int(sys.argv[1])
    else:
        example = 1
    data = get_datapoints2(example)
    print(data)
    print(find_route(data))

