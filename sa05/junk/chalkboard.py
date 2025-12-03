from cs1lib import *

program_counter = 0
old_x = 0
old_y = 0
cur_x = 0
cur_y = 0
drawn = False
def mousein(x, y):
    global old_x, old_y
    old_x, old_y = x, y
    drawn = True
    #print("entered", old_x, old_y)
    return old_x, old_y

def on_release(x, y):
    global cur_x, cur_y
    cur_x, cur_y = x, y
    #print("left", cur_x, cur_y)
    return cur_x, cur_y


# def on_release(old_x, old_y):
#     #print("Mouse up! " + str(old_x) + " " + str(old_y))

def extractor():
    mousein(old_x, old_y)

    

# old_x, old_y = mousein(100, 100)

def chalkboard():
    global program_counter
    # , old_x, old_y, cur_x, cur_y, drawn

    # if program_counter == 0:
    #     clear()
    #     print("called once")


    # set_fill_color(0, 0, 0)
    # draw_rectangle(-1, -1, 402, 402)


    set_stroke_width(3)
    set_stroke_color(0, 0, 0)
    # set_stroke_color(1, 1, 1)
    
    draw_point(old_x, old_y)
    draw_point(cur_x, cur_y)
    # cur_x = old_x
    # cur_y = old_y
    draw_line(old_x, old_y, cur_x, cur_y)
    # draw_circle(old_x, old_y, 50)
    #print(old_x, old_y)
    set_stroke_width(0)
    # #print(mousein())
    program_counter += 1



print(old_x, old_y, old_x, old_y)

start_graphics(chalkboard, 100,
            #    mouse_move=mousein,
               mouse_press=mousein,
               mouse_release=on_release,
            #    framerate=10
               )

