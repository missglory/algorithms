#Uses python3

import sys, os
import queue

def bfs(adj, x, q, shortest):
    q.append(x)
    while len(q):
        x = q.pop(0)
        for i in adj[x]:
            if shortest[i] >= (int)(2e9):
                q.append(i)
                shortest[i] = shortest[x] + 1
        


def distance(adj, s, t):
    #write your code here
    n = len(adj)
    q = []
    shortest = [(int)(2e9)] * n
    shortest[s] = 0
    bfs(adj, s, q, shortest)
    return shortest[t] if shortest[t] < (int)(2e9) else -1

if __name__ == '__main__':

    # sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\test\01', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
