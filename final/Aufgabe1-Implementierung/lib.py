
import math

def get_datapoints(example: str = "data/wenigerkrumm1.txt") -> list[tuple[float]]:
    """Opens example file, reads data and returns it as a list of coordinates (tuples (x, y))"""
    with open(example) as f:
        return [tuple([float(i) for i in l.strip().split()]) for l in f.readlines()]

def dist(p0: tuple[float], p1: tuple[float]):
    """Calculates distances between two points"""
    return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

def angle(p0: tuple[float], p1: tuple[float], p2: tuple[float]) -> float:
    """Calculates angle between three points in degrees"""
    scalar_product = (p1[0] - p0[0]) * (p2[0] - p1[0]) + (p1[1] - p0[1]) * (p2[1] - p1[1])
    dist_0_1 = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    dist_1_2 = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    # we calculate the angle between two vectors: arccos(scalar product / product of length of vectors)
    rhs = scalar_product / (dist_0_1 * dist_1_2)
    # limits (result may be slightly higher/lower)
    if rhs > 1: rhs = 1
    if rhs < -1: rhs = -1
    return math.degrees(math.acos(rhs))
