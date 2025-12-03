from collections import deque
from load_graph import create_vertex_dictionary


def bfs(graph, start, end):
    visited = {}
    explore = deque()                       # Initialize a queue for BFS
    path = [start]
    print(visited)
    for i in graph:
        # print(graph)
        explore.append(i)
        # explore.append(start)
        # explore.append(end)
    explore.append(end)
        # next = explore.popleft()
    toworkon = explore
    for j in toworkon:    
        if next == end:
            path.append(end)
            return path
        if j not in visited:
            visited[graph[i].name] = graph[i].xlocation, graph[i].ylocation
        explore.popleft()
        # print("sdabsdoia")

        visited[graph[i].name] = graph[i].xlocation, graph[i].ylocation
    print("visited")
    # return path


# print(bfs(create_vertex_dictionary("dartmouth_graph.txt"), "Sanborn", "FDA"))
bfs(create_vertex_dictionary("dartmouth_graph.txt"), "Sanborn", "FDA")
        













from collections import deque
from load_graph import create_vertex_dictionary

def bfs(graph, start, end):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        current_vertex = graph[current]

        if current == end:
            break

        for neighbor in current_vertex.edges:
            name = neighbor.name
            if name not in visited:
                visited[name] = current
                queue.append(name)

    # Build path
    if end not in visited:
        return None

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = visited[node]

    path.reverse()
    return path


# Example:
graph = create_vertex_dictionary("dartmouth_graph.txt")
print(bfs(graph, "Butterfield", "FDA"))
