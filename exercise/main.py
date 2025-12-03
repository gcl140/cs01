def main(x):
    if x <= 0:
        return 20
    print(x)
    return main(x -1)
    # main(x -1)
   
    

y = main(3)
print(y)
arr = []