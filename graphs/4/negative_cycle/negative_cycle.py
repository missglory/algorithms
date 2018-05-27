#Uses python3

import sys, os


def BellmanFord(adj,cost,dist):
    #repeat |V - 1| times:
    #  try to relax all edges =>
    #O(|V|*|E|), |V|, |E| - num of nodes/edges 
    res = 0
    for k in range(n - 1):
        f = False
        for i in range(n):
            for j in range(len(adj[i])):
                c = adj[i][j]
                # dist[c] = min(dist[c], dist[i] + cost[i][j])
                if dist[c] > dist[i] + cost[i][j]:
                    f = True
                    res = 1
                    dist[c] = dist[i] + cost[i][j]
        if not f:
            break
    return res

# def bf2(adj,cost,dist):
#     for i in range(n):
#         for j in range(len(adj[i])):
#             c = adj[i][j]
#             if dist[c] > dist[i] + cost[i][j]:
#                 return 1
#     return 0

def negative_cycle(adj, cost):
    #write your code here
    n = len(adj)
    dist = [(int)(2e9)] * n
    par = [-1] * n
    dist[0] = 0
    BellmanFord(adj,cost, dist)
    return BellmanFord(adj,cost,dist)


if __name__ == '__main__':
    # sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\test\t1', 'r')
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
    print(negative_cycle(adj, cost))
