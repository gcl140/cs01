from cs1lib import *
from load_graph import create_vertex_dictionary
from bfs import bfs

graph = create_vertex_dictionary("dartmouth_graph.txt")
background = load_image("dartmouth_map.png")

start_vertex = None
end_vertex = None
current_hover = None

def mouse_press(x, y):
    # You only set the start candidate here
    pass  # real selection happens on release

def mouse_release(x, y):
    global start_vertex
    for key in graph:
        v = graph[key]
        if v.is_on_vertex((x, y)):
            start_vertex = v
            print("Start picked:", v.name)
            break

def mouse_move(x, y):
    global current_hover, end_vertex
    hover_candidate = None
    for key in graph:
        v = graph[key]
        if v.is_on_vertex((x, y)):
            hover_candidate = v
            break
    current_hover = hover_candidate

    # Only set goal if start already picked AND hovering something else
    if start_vertex and current_hover and current_hover != start_vertex:
        end_vertex = current_hover
    else:
        end_vertex = None  # no valid goal

def main():
    clear()
    draw_image(background, 0, 0)

    # draw everything in blue
    for key in graph:
        v = graph[key]
        v.draw_all_edges(0, 0, 1)
        v.draw_vertex(0, 0, 1)

    # red highlight for hover
    if current_hover:
        current_hover.draw_vertex(1, 0, 0)

    # if start picked, draw it yellow
    if start_vertex:
        start_vertex.draw_vertex(1, 1, 0)

    # if valid goal selected, compute BFS path
    # if start_vertex and end_vertex:
    #     path = bfs(start_vertex, end_vertex)
    #     if path:
    #         # for v in path:
    #         for v in range(len(path) - 1):
    #             path[v].draw_vertex(0, 1, 0)  # green path
    #             # if v != len(path) - 1:
    #             path[v].draw_edges(0, 1, 0, path[v - 1])  # green path

    if start_vertex and end_vertex:
        path = bfs(start_vertex, end_vertex)
        if path:
            # color vertices green
            for v in path:
                v.draw_vertex(0, 1, 0)

            # color edges green
            for i in range(len(path) - 1):
                v1 = path[i]
                v2 = path[i + 1]
                set_stroke_color(0, 1, 0)
                draw_line(v1.xlocation, v1.ylocation, v2.xlocation, v2.ylocation)

start_graphics(main, width=1012, height=811,
               mouse_press=mouse_press,
               mouse_release=mouse_release,
               mouse_move=mouse_move)
