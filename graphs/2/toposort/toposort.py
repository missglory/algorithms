#Uses python3

import sys

def dfs(adj, used, order, removed, x):
    used[x] = True
    for c in adj[x]:
        if removed[c]: continue
        if used[c]:
            raise Exception(x,c)
        else:
            dfs(adj,used,order,removed,c)
    removed[x] = True
    order.append(x)
    #write your code here
    # pass


def toposort(adj):
    n = len(adj)
    used = [0] * n
    order = []
    removed = [0] * n
    adj_reverse = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(adj[i])):
            adj_reverse[adj[i][j]].append(i)
    #write your code here
    for i in range(n):
        if not removed[i]:
            dfs(adj_reverse,used,order,removed,i)
    return order

if __name__ == '__main__':
    # sys.stdin = open(r'C:\Users\Admin\Desktop\crsra\graphs\2\toposort\test\01', "r")
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

