#strings, lists, are heaps not stacks. global, local and instance (leave for a moment)
#stack.................... heap: ball at 1048 location. in ball, with (b = Ball(42, 107)) 
# allocates the space, and calls the init method which copies the value 42 to the heap for x
# and y for 107 in the heap. but it had already a vx and vy. Ball(will have the data of the location
# ) of the x and y in the heap. and b is stored as a stack b: 1048. that's why to call b an action
# from b. eg, b.update() 


# lists also got into heap