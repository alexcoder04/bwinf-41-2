
from lib import get_datapoints, dist, angle

import math

def nearest_neighbor_with_angle_constraint(points):
    unvisited = set(range(1, len(points)))
    path = [0]
    curr_node = 0

    while unvisited:
        min_dist = float('inf')
        best_node = None
        for neighbor in unvisited:
            dist = math.dist(points[curr_node], points[neighbor])
            if dist < min_dist:
                angle = compute_angle(points[curr_node], points[path[-1]], points[neighbor])
                if angle >= 90:
                    min_dist = dist
                    best_node = neighbor

        if best_node is None:
            if not path:
                return None
            curr_node = path.pop()
            unvisited.add(curr_node)
        else:
            path.append(best_node)
            unvisited.remove(best_node)
            curr_node = best_node

    path.append(0)
    return path

def compute_angle(p1, p2, p3):
    return angle(p1, p2, p3)
    #a = math.dist(p2, p3)
    #b = math.dist(p1, p3)
    #c = math.dist(p1, p2)
    #if a == 0 or c == 0:
    #    return 180
    #else:
    #    return math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))

if __name__ == "__main__":
    data = get_datapoints(6)
    print(nearest_neighbor_with_angle_constraint(data))
