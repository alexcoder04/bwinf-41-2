
from lib import get_datapoints, angle, dist

data = get_datapoints(7)

def check_point(data, i):
    for f in range(len(data)):
        if f == i:
            continue
        for t in range(len(data)):
            if t == i:
                continue
            if angle(data[f], data[i], data[t]) <= 90:
                return True
    return False

for i in range(len(data)):
    if not check_point(data, i):
        print(data[i])
