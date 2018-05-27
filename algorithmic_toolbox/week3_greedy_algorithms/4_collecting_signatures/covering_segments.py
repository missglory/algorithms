# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = [segments[0][1]]
    #write your code here
    for i in range(1, len(segments)):
        if segments[i][0] <= points[len(points)-1]: continue
        points.append(segments[i][1])
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments.sort(key = lambda x: x[1])
    # print (segments[0][1])
    # print (segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
