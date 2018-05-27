#Uses python3

import sys, os
import queue, heapq


class pq:
    def __init__(self):
        self._q = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._q, (priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._q)

def distance(adj, cost, s, t):
    n = len(adj)
    dist = [(int)(2e9)] * n
    dist[s] = 0
    par = [-1] * n
    q = pq()
    q.push(s, 0)
    while len(q._q):
        x = q.pop()
        for i in range(len(adj[x[-1]])):
            c = adj[x[-1]][i]
            relax = cost[x[-1]][i] + dist[x[-1]]
            if relax < dist[c]:
                dist[c] = relax
                par[c] = x[-1]
                q.push(c, relax)
    #write your code here
    return dist[t] if dist[t] < (int)(2e9) else -1


if __name__ == '__main__':
    # sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\test\01', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
