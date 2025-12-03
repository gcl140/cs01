from collections import deque
# from load_graph import create_vertex_dictionary


def bfs(graph, start, end):
    queue = deque()
    queue.append(start)
    visited = {start: None}
    length = len(queue)
    while length > 0:
        current = queue.popleft()
        its_vertex = graph[current]

        if current == end:
            print("You've arrived!")
            break

        for neighbour in its_vertex.edges:
            if neighbour.name not in visited:
                visited[neighbour.name] = current # adding their names
                queue.append(neighbour.name) # add them to the reviewing queue
    print(visited)
    if end not in visited:
        return None
    
    
    #now that we have our queue
    path = []
    astep = end         # start from the back


    while astep is not None:
        path.append(astep)
        astep = visited[astep] #set value to key

    for i in range(len(path) // 2):
        path[i], path[len(path) - 1 - i] = path[len(path) - 1 - i], path[i]
    return path

# print(bfs(create_vertex_dictionary("dartmouth_graph.txt"), "FDA", "East Wheelock"))
        