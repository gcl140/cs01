# def sum_multiples(glist, p):
#     if not glist:  # base case: empty list
#         return 0
    
#     head = glist[0]
#     rest = glist[1:]
    
#     if head % p == 0:
#         return head + sum_multiples(rest, p)
#     else:
#         return sum_multiples(rest, p)


def sum_multiples(glist, p):
    if len(glist) == 1:
        if glist[0] % p == 0:
            sum = glist[0]
            return sum
        else:
            sum = 0
            return sum

    else:
        if glist[0] % p == 0:
            first = glist[0]
        else:
            first = 0
        sum = 0

    return first + sum_multiples(glist.remove(glist[0]), p) + sum


print(sum_multiples([1, 2, 3, 4, 5, 6], 2))
        
    # else:
    #     if glist[0] % p == 0:
    #         sum = glist[0] + sum_multiples(glist[1:], p)
    #         return sum
    #     else:
    #         sum = 0 + sum_multiples(glist[1:], p)
    #         return sum