class Edge:
    def __init__(self, dst, weight):
        self.dst, self.weight = dst, weight

    def __lt__(self, e):
        return self.weight > e.weight


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = [[] for _ in range(V)]

    def add_edge(self, src, dst, weight):
        self.E[src].append(Edge(dst, weight))


class TreeDiameter:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.diameter = None
        self.fathest_pair = None

    def run(self):
        _, v1 = self.calc_farthest(0, -1)
        diameter, v2 = self.calc_farthest(v1, -1)
        self.diameter = diameter
        self.fathest_pair = (v1, v2)
        return diameter

    def calc_farthest(self, target: int, par: int = -1):
        dists = [None] * self.graph.V
        stack = [(target, par)]

        while stack:
            v, par = stack[-1]
            if dists[v] is None:
                dists[v] = (0, v)
                for child in self.graph.E[v]:
                    if child.dst == par:
                        continue
                    stack.append((child.dst, v))
            else:
                stack.pop()
                ret_dist, ret_v = dists[v]
                for child in self.graph.E[v]:
                    if child.dst == par:
                        continue
                    cand_dist, cand_v = dists[child.dst]
                    if cand_dist + child.weight > ret_dist:
                        ret_dist = cand_dist + child.weight
                        ret_v = cand_v
                dists[v] = (ret_dist, ret_v)

        return dists[target]


def aoj():
    N = int(input())
    graph = Graph(N)
    for _ in range(N-1):
        s, t, w = map(int, input().split())
        graph.add_edge(s, t, w)
        graph.add_edge(t, s, w)
    diam = TreeDiameter(graph)
    print(diam.run())


if __name__ == "__main__":
    aoj()