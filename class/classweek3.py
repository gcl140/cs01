from cs1lib import *

has_called = False
def mydraw():
    global circle_x, circle_y, radius, has_called
    if has_called == False:
        clear() 
    draw_circle(circle_x, circle_y, radius)
    # if circle_x < 400 or circle_y < 400 or radius < 200:
    if circle_x < 400 and circle_y < 400 and radius < 200:
        circle_x += 10
        circle_y += 10
        radius += 10
    # circle_x += 5
    # circle_y += 5
    # radius += 5
    has_called = True

circle_x = 20
circle_y = 20
radius = 50
# start_graphics(mydraw)
# start_graphics(mydraw, framerate=1)






# ============================================

mouse_col = -1
mouse_row = -1
def mouse_moved(mx, my):
    global mouse_col, mouse_row
    mouse_col = mx // SSIZE
    mouse_row = my // SSIZE
    print(mouse_row, mouse_col)
    # print("Mouse moved to", mx, my)
    # pass

def key_down(key):
    pass
    # print("Key pressed:", key)

SSIZE = 40

def draw_square(c, r, color):
    if color == "white":
        set_fill_color(1, 1, 1)
        set_stroke_color(0, 0, 0)
    elif color == "gray":
        set_fill_color(0.5, 0.5, 0.5)
        set_stroke_color(0, 0, 0)
    else:
        set_fill_color(0, 0, 0)
    draw_rectangle(c * SSIZE, r * SSIZE, SSIZE, SSIZE)

def draw_chessboard():
    global has_called, mouse_col, mouse_row
    clear()
    r = 0
    while r < 8:
        c = 0
        while c < 8:
            if c == mouse_col and r == mouse_row:
                draw_square(c , r, "gray")
            
            elif (c + r) % 2 == 0:
                draw_square(c , r, "white")
            # elif c == mouse_col and r == mouse_row:
            #     draw_square(c , r, "gray")
            
            else:
                draw_square(c , r, "black")
            c += 1
        r += 1
    has_called = True


start_graphics(draw_chessboard, mouse_move=mouse_moved, key_press=key_down, width=SSIZE*8, height=SSIZE*8)
    