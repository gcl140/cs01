class Vertex:
    def __init__(self, name, location, edges):
        self.name = name
        self.location = location
        self.edges = edges  # edges is expected to be a list of Vertex instances

    def __str__(self):
        return self.name + str(self.edges)
    
# if __name__ == "__main__":
#     from collections import deque
#     a = Vertex("A", ["B", "C"])
#     graph_dict = {}
#     graph_dict["A"] = Vertex("A", ["B", "C"])
#     graph_dict["B"] = Vertex("B", ["A", "D"])
#     graph_dict["C"] = Vertex("C", ["A", "B", "D", "E"])
#     graph_dict["D"] = Vertex("D", ["A", "B", "D"])
#     graph_dict["E"] = Vertex("E", ["C", "D", "F"])
#     graph_dict["F"] = Vertex("F", ["E"])
#     for key in graph_dict:
#         print(graph_dict[key])
#     print(a)

#     explore = deque()
#     explore.append("A")
#     explore.append("D")
#     print(explore)
    
#     # loop here
#     current = explore.popleft()

#     print(current)
#     print(explore)

#     # add neighbors to explore, but be careful to avoid duplicates
#     # reached_from = {}
#     # example: B came from A, so store 
#     # if B in reached_from:
#     current_vertex = graph_dict[current]
#     print(current_vertex)
#     explore.append(current_vertex.edges[0])
#     explore.append(current_vertex.edges[1])