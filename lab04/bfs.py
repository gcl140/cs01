from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited = {start: None}   # store parent pointers

    while len(queue) > 0:
        current = queue.popleft()
        if current == end:
            break
        for neighbour in current.edges:  # neighbour is already a Vertex
            if neighbour not in visited:
                visited[neighbour] = current
                queue.append(neighbour)

    if end not in visited:
        return None

    # Reconstruct path from end -> start
    path = []
    astep = end

    while astep is not None:
        # path.append(astep.name)
        path.append(astep)
        astep = visited[astep]

    # manual reverse (since you hate ::-1)
    for i in range(len(path) // 2):
        path[i], path[len(path) - 1 - i] = path[len(path) - 1 - i], path[i]

    return path
