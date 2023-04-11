
import math

def get_datapoints(example: int = 1) -> list[list[float]]:
    with open(f"data/wenigerkrumm{example}.txt") as f:
        return [[float(i) for i in l.strip().split()] for l in f.readlines()]

def get_datapoints2(example: int = 1) -> list[tuple[float]]:
    with open(f"data/wenigerkrumm{example}.txt") as f:
        return [tuple([float(i) for i in l.strip().split()]) for l in f.readlines()]

def dist(p0: tuple[float], p1: tuple[float]):
    return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

def angle(p0: tuple[float], p1: tuple[float], p2: tuple[float]) -> float:
    scalar_product = (p1[0] - p0[0]) * (p2[0] - p1[0]) + (p1[1] - p0[1]) * (p2[1] - p1[1])
    dist_0_1 = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    dist_1_2 = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    rhs = scalar_product / (dist_0_1 * dist_1_2)
    if rhs > 1:
        rhs = 1
    if rhs < -1:
        rhs = -1
    return math.degrees(math.acos(rhs))

def route_length(data, route):
    total = 0
    for i in range(len(route) - 1):
        total += dist(data[route[i]], data[route[i+1]])
    return total
