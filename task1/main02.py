#!/usr/bin/env python3

import sys
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

def find_possible_routes(points: list[list[int]], route: list[int] = []):
    if len(route) == len(points):
        global total
        total += 1
        sys.stderr.write(str(total) + "\n")
        sys.stdout.write(str(route) + "\n")
        return

    if len(route) <= 1:
        for i in range(len(points)):
            if i in route:
                continue
            find_possible_routes(points, route + [i])
        return
    
    for i in range(len(points)):
        if i in route:
            continue
        a = angle(points[route[-2]], points[route[-1]], points[i])
        #if a >= 1.5708:
        if a >= 1.22:
            continue
        find_possible_routes(points, route + [i])

if __name__ == "__main__":
    data = get_datapoints(4)
    #print(data)
    find_possible_routes(data)
