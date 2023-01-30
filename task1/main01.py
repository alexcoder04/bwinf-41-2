#!/usr/bin/env python3

import math

total = 0

def get_datapoints(example: int = 1) -> list[list[int]]:
    with open(f"wenigerkrumm{example}.txt") as f:
        return [[float(i) for i in l.strip().split()] for l in f.readlines()]

def angle(p0: list[int], p1: list[int], p2: list[int]) -> float:
    scalar_product = (p1[0] - p0[0]) * (p2[0] - p1[0]) + (p1[1] - p0[1]) * (p2[1] - p1[1])
    dist_0_1 = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    dist_1_2 = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return math.acos((scalar_product) / (dist_0_1 * dist_1_2))

def possible_routes(points: list[list[int]], route: list[list[int]] = []) -> list[list[list[int]]]:
    if len(points) == 0:
        global total
        total += 1
        print(total)
        return route

    routes = []
    #print(len(route))

    if len(route) <= 1:
        for p in points:
            this_points = points.copy()
            this_points.remove(p)
            routes += possible_routes(this_points, route + [p])
        return routes
    
    for p in points:
        a = angle(route[-2], route[-1], p)
        if a >= 90:
            continue
        this_points = points.copy()
        this_points.remove(p)
        routes += possible_routes(this_points, route + [p])

    return routes

if __name__ == "__main__":
    data = get_datapoints(4)
    #print(data)
    possible = possible_routes(data)
    for r in possible:
        print(r)
