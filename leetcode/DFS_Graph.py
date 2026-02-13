class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        if not current_vertex:
            return

        visited.append(current_vertex)
        childs = sorted(self.graph[current_vertex])
        for child in childs:
            if child and child not in visited:
                self.depth_first_search_r(visited, child)

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)

    def __repr__(self) -> str:
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
        return result
