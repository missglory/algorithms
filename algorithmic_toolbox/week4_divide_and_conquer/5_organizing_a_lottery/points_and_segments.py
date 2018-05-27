# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    di1, di2 = {}, {}
    c, d = 0, 0
    for i in starts:
        di1[i] = c
        c += 1
    for i in ends:
        di2[i] = d
        d += 1
    
    points = data[2 * n + 2:]
    dp = [0] * len(points)
    
    print(dp)
    for i in range(len(starts)):
        
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
