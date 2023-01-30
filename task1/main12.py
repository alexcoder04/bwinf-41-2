#!/usr/bin/env python3

import random

from lib import get_datapoints, dist, angle

def closest_point(data: list[float], route: list[int]) -> int:
    closest = None
    min_dist = 1000000
    for i in range(len(data)):
        if i in route:
            continue
        d = dist(data[route[-1]], data[i])
        try:
            route[-2]
        except Exception:
            a = 0
        else:
            a = angle(data[route[-2]], data[route[-1]], data[i])
        if d < min_dist and a <= 90:
            min_dist = d
            closest = i
    return closest

def run(data, start):
    route = [start]

    for _ in range(len(data) - 1):
        c = closest_point(data, route)
        if c is None:
            #print(data)
            print(route)
            return []
        route.append(c)
        #print(route)

    #print(route)
    return [route]

def program(example, verbose):
    data = get_datapoints(example)
    all_routes = []

    for i in range(len(data)):
        all_routes += run(data, i)

    if verbose:
        #for i in all_routes:
        #    print(i)
        return
    return all_routes[0]

if __name__ == "__main__":
    program(6, True)
