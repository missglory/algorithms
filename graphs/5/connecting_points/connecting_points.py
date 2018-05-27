#Uses python3
import sys, os
import math
inf = 10**9


def dist(i, j): return math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

def findmin(q, r):
    """
    args:
    q - array based queue
    r - boolean map of removed elems 
    """
    n = len(q)
    ans, ind = inf, 0
    for i in range(n):
        if not r[i] and ans > q[i]:
            ans = q[i]
            ind = i
    r[ind] = True
    return ans, ind
    
#Prim's algo
def minimum_distance(x, y):
    n = len(x)
    cost, parent = [inf] * n, [-1] * n
    cost[0] = 0
    q = [inf] * n
    r = [False] * n
    q[0] = 0
    lenq = len(q)
    while lenq:
        _, j = findmin(q, r)
        lenq -= 1
        for i in range(n):
            if i == j: continue
            relax = dist(i,j)
            if not r[i] and cost[i] > relax:
                q[i] = relax
                cost[i] = relax
    return sum(cost)


def prep(n, x, y):
    pass

if __name__ == '__main__':
    # sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\test\02', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    # print(minimum_distance(x,y))
