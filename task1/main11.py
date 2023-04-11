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
    if closest is None:
        raise Exception("arghhhh")
    return closest

data = get_datapoints(7)

route = [0]

for i in range(len(data) - 1):
    route.append(closest_point(data, route))

print(route)
print(len(route), len(data))
