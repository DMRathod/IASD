from collections import defaultdict

import Connecting_point as cp


# Creating the physical location as connecting points
def add_edges_on_node(node_one, node_two, graph):
    graph[node_one].append([node_two, 0])
    graph[node_two].append([node_one, 0])


def add_edges(edges, graph):
    for node_one, node_two in edges:
        add_edges_on_node(node_one, node_two, graph)


class CreateConnectingPoint:
    connecting_point_adjacency_list = defaultdict(list)
    list_of_all_connecting_points = []
    a = cp.ConnectingPoint(11, 59, 'a')
    b = cp.ConnectingPoint(12, 45, 'b')
    c = cp.ConnectingPoint(39, 41, 'c',)
    d = cp.ConnectingPoint(50, 58, 'd',)
    e = cp.ConnectingPoint(70, 60, 'e', 1)
    f = cp.ConnectingPoint(69, 39, 'f',)
    g = cp.ConnectingPoint(55, 31, 'g', 1)
    h = cp.ConnectingPoint(43, 20, 'h', 1)
    i = cp.ConnectingPoint(25, 18, 'i', 2)
    j = cp.ConnectingPoint(45, 5, 'j')
    k = cp.ConnectingPoint(71, 20, 'k', )
    l = cp.ConnectingPoint(88, 30, 'l', )
    m = cp.ConnectingPoint(90, 10, 'm',)
    n = cp.ConnectingPoint(84, 40, 'n', 3)
    o = cp.ConnectingPoint(102, 20, 'o')
    p = cp.ConnectingPoint(114, 5, 'p')
    q = cp.ConnectingPoint(95, 0, 'q')
    r = cp.ConnectingPoint(102, 32, 'r', 2)
    s = cp.ConnectingPoint(27, 2, 's', 1)
    t = cp.ConnectingPoint(5, 20, 't')
    edges = [(a, b), (a, d), (b, d), (b, c), (c, d),
             (b, t), (t, i), (i, c),
             (i, h), (i, s), (h, s), (h, j), (s, j),
             (h, g), (c, g), (f, g), (g, k), (h, k),
             (f, n), (f, l), (k, l), (l, r), (k, m), (m, o), (r, o), (n, r), (l, m),
             (m, p), (m, q), (q, p), (p, o),
             (d, e), (d, f), (d, n), (e, n)]
    add_edges(edges, connecting_point_adjacency_list)
    list_of_all_connecting_points.extend([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t])

    def __init__(self):
        pass
        # self.list_of_all_connecting_points.extend([self.a, self.b, self.c, self.d,self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p, self.q, self.r, self.s, self.t])


    def get_connecting_points(self):
        return self.list_of_all_connecting_points

    def get_graph_of_connecting_points(self):
        return self.connecting_point_adjacency_list







