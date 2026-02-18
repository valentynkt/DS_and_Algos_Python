class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set(v)
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = u
