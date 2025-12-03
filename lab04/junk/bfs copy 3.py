from collections import deque
from load_graph import create_vertex_dictionary


def bfs(graph, start, end):
    visited = {}
    explore = deque()                       # Initialize a queue for BFS
    # print(graph)
    starthere = graph[start]
    for location in graph:
        visited[location] = graph[location].edges
        if graph[end] in graph[location].edges:
            print(location)
            break
        # print(graph[location].edges)
        # print(location)
    print(visited)

# print(bfs(create_vertex_dictionary("dartmouth_graph.txt"), "Sanborn", "FDA"))
bfs(create_vertex_dictionary("dartmouth_graph.txt"), "Sanborn", "FDA")
        