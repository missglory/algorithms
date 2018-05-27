#Uses python3

import sys

def dfs(adj, x, used):
    used[x] = True
    for c in adj[x]:
        if not used[c]:
            dfs(adj, c, used)

def number_of_components(adj):
    result = 0
    #write your code here
    used = [False] * len(adj)
    for i in range(len(adj)):
        if not used[i]:
            dfs(adj, i, used)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
