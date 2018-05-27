# python3

import sys, os
inf = 10**9

class Edge:

    def __init__(self, u, v, capacity, id = 0):
        self.id = id
        self.u = u
        self.v = v
        self.c = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity, len(self.edges))
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        backward_edge = Edge(to, from_, 0, len(self.edges))
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def bfs(g, S, T):#shortest, path):
    '''
    g: flow graph
    S: source
    T: sink
    '''
    q = [S]
    shortest = [inf] * g.size()
    shortest[S] = 0
    prev = [None] * g.size()
    while len(q):
        x = q.pop(0)
        for i in g.get_ids(x):
            i = g.get_edge(i)
            assert i.u == x
            if i.flow == i.c: continue
            if shortest[i.v] >= inf: # shortest[x] + 1:
                shortest[i.v] = shortest[x] + 1
                prev[i.v] = i
                q.append(i.v)
    if not prev[T]:
        return []
    pos = prev[T]
    flow = inf
    while pos:
        flow = min(flow, pos.c - pos.flow)
        pos = prev[pos.u]
    pos = prev[T]
    while pos:
        g.add_flow(pos.id, flow)
        pos = prev[pos.u]
    return prev

        



def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    path = [to]
    while path:
        path = bfs(graph, from_, to)
        flow += path[1]
    return flow


if __name__ == '__main__':
    sys.stdin = open(os.path.abspath(os.path.dirname(__file__)) + r'\tests\01', 'r')
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
