#Uses python3
import sys, os
import math

class DisjointSets:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
    def get_parent(self, i):
        if not i == self.parent[i]:
            self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]
    def merge(self, x, y):
        i, j = self.get_parent(x), self.get_parent(y)
        if i == j:return 0
        if self.rank[i] >= self.rank[j]:
            self.parent[j] = i
            if self.rank[j] == self.rank[i]:
                self.rank[i] += 1
            self.size[i] += self.size[j]
        else:
            self.parent[i] = j
            self.size[j] = self.size[i]
        return 1

def clustering(x, y, k, edges):
    #write your code here
    n = len(x)
    ind = 0
    count = n
    ds = DisjointSets(n)
    while ind < len(edges):
        count -= ds.merge(edges[ind][0], edges[ind][1])
        if count < k: break
        ind += 1
    return edges[ind][2]
    


def prep_edges(x, y):
    n = len(x)
    edges = []
    dist = lambda i, j: math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    for i in range(n):
        for j in range(i, n):
            if i == j: continue
            edges.append([i,j,dist(i,j)])
    return edges

if __name__ == '__main__':
    # sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\test\01', 'r')
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    edges = prep_edges(x, y)
    edges.sort(key = lambda x: x[2])
    print("{0:.9f}".format(clustering(x, y, k, edges)))
