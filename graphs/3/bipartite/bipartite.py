#Uses python3

import sys, os
import queue



def bfs(adj, x, q, mp):
    q.append(x)
    while len(q):
        x = q.pop(0)
        for i in adj[x]:
            if mp[i] == mp[x]:
                return 0
            if mp[i] == 2:
                q.append(i)
                mp[i] = mp[x] ^ 1
    return 1


def bipartite(adj):
    #write your code here
    n = len(adj)
    mp = [2] * n
    q = []
    for i in range(n):
        if mp[i] == 2:
            mp[i] = 0    
            if not bfs(adj, 0, q, mp):
                return 0
    # for i in range(n):
    #     for j in adj[i]:
    #         if mp[i] == mp[j]:
    #             return 0
    return 1

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
    print(bipartite(adj))
