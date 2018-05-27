#Uses python3

import sys, os
import queue
inf = 10**19

#WA 19
def BellmanFord(adj, cost, d, shortest, rchbl, is_second = False):
    n = len(adj)
    for _ in range(n - 1):
        f = False
        for i in range(n):
            for j in range(len(adj[i])):
                c = adj[i][j]
                if not rchbl[c]: continue
                if d[c] > d[i] + cost[i][j]:
                    if is_second: return c
                    d[c] = d[i] + cost[i][j]
                    f = True
                    shortest[c] = 0
        if not f:
            break
    return -1
        
def dfs(adj, s, u, rchbl, filler = 1):
    u[s] = True
    rchbl[s] = filler
    for i in adj[s]:
        if not u[i]:
            rchbl[i] = 1
            dfs(adj, i, u, reachable, filler)
        


def shortet_paths(adj, cost, s, d, reachable, shortest):
    #write your code here
    n = len(adj)
    u = [False] * n
    dfs(adj, s, u, reachable)
    BellmanFord(adj, cost, d, shortest, reachable)
    for i in range(n): shortest[i] = 1
    cycle_node = BellmanFord(adj, cost, d, shortest, reachable)
    for i in range(n): u[i] = False
    if not cycle_node == -1: dfs(adj, cycle_node, u, shortest, filler = 0)
    return shortest

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
    s = data[0]
    s -= 1
    d = [inf] * n
    reachable = [0] * n
    shortest = [1] * n
    d[s] = 0
    shortet_paths(adj, cost, s, d, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(d[x])

