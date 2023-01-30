
import math

def get_datapoints(example: int = 1) -> list[list[int]]:
    with open(f"data/wenigerkrumm{example}.txt") as f:
        return [[float(i) for i in l.strip().split()] for l in f.readlines()]

def dist(p0: list[float], p1: list[float]):
    return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

def angle(p0: list[float], p1: list[float], p2: list[float]) -> float:
    scalar_product = (p1[0] - p0[0]) * (p2[0] - p1[0]) + (p1[1] - p0[1]) * (p2[1] - p1[1])
    dist_0_1 = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    dist_1_2 = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    rhs = scalar_product / (dist_0_1 * dist_1_2)
    if rhs > 1:
        rhs = 1
    if rhs < -1:
        rhs = -1
    return math.degrees(math.acos(rhs))
