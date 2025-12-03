def idealvalues(low, high):
    if low >= high:
        return []
    p3 = 1
    output = set()
    while p3 <= high:
        p5 = 3
        while p5 <= high:
            val = p3 * p5
            if val >= low and (p5 >= 5 and p3 >= 3):
                output.add(val)
            p5 *=5
        p3 *=3
    return sorted(output)


    # for i in range(low, high+1):
    #     for j in range(low, high):
            

# print(idealvalues(225, 400))