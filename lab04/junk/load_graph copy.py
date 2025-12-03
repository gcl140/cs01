from collections import deque
from vertex import Vertex

def idk():
    a = Vertex("A", ["B", "C"])
    graph_dict = {}
    graph_dict["A"] = Vertex("A", ["B", "C"])
    graph_dict["B"] = Vertex("B", ["A", "D"])
    graph_dict["C"] = Vertex("C", ["A", "B", "D", "E"])
    graph_dict["D"] = Vertex("D", ["A", "B", "D"])
    graph_dict["E"] = Vertex("E", ["C", "D", "F"])
    graph_dict["F"] = Vertex("F", ["E"])
    for key in graph_dict:
        print(graph_dict[key])
    print(a)

    explore = deque()
    explore.append("A")
    explore.append("D")
    print(explore)

    # loop here
    current = explore.popleft()

    print(current)
    print(explore)

    # add neighbors to explore, but be careful to avoid duplicates
    # reached_from = {}
    # example: B came from A, so store 
    # if B in reached_from:
    current_vertex = graph_dict[current]
    print(current_vertex)
    explore.append(current_vertex.edges[0])
    explore.append(current_vertex.edges[1])

def load_graph():
    graph_dict = {}
    for line in open("dartmouth_graph.txt"):
        parts = line.strip().split()
        for i in range(len(parts)):
            if parts[i] == ";":
                name = parts[0]
                location = parts[1:i]
                edges = parts[i+1:]
                graph_dict[name] = Vertex(name, location, edges)
                break

        print(parts)
        # name = parts[0]
        # edges = parts[1:]
        # graph_dict[name] = Vertex(name, edges)

load_graph()