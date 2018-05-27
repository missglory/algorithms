#Uses python3

import sys

sys.setrecursionlimit(200000)

# def dfs(adj, used, order, d, x):
def dfs(*args):
    adj, used, order, d, x = args 
    used[x] = True
    if not order is None:
        order[x][0] = d[0]
    d[0] += 1
    for c in adj[x]:
        if not used[c]:
            dfs(adj, used, order, d, c)
    if not order is None:
        order[x][1] = d[0]
    d[0] += 1
    


def number_of_strongly_connected_components(adj):
    result = 0
    n = len(adj)
    adj_r = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(adj[i])):
            adj_r[adj[i][j]].append(i)
    used = [False] * n
    order = [[-1, -1, i] for i in range(n)]
    d = [1]

    for i in range(n):
        if not used[i]:
            dfs(adj_r, used, order, d, i)
    used = [False] * n
    order.sort(key = lambda x: x[1], reverse=True)
    scc_order = [x[2] for x in order]
    for i in scc_order:
        if not used[i]:
            dfs(adj, used, None, [1], i)#order[i][2])
            result += 1
    return result

if __name__ == '__main__':
    # sys.stdin = open(r'C:\Users\Admin\Desktop\crsra\graphs\2\strongly_connected\test\s1', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
