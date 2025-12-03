def sum_multiples(glist, p):
    if glist == []: # base case, empty list
        return 0
    head = glist[0]
    rest = glist[1:]

    if head % p == 0:
        return head + sum_multiples(rest, p)
    else: 
        return sum_multiples(rest, p)
    

print(sum_multiples([1, 2, 3, 4, 5, 6], 2))