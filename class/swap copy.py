
def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp
    # return the_list

mylist = [95, 82, 61, 12, 22, 32, 45, 72, 56]

pos = 0
while pos < len(mylist) - 1:
    # min = mylist[0]
    min_idx = pos

    for i in range(pos, len(mylist)):
        if mylist[i] < mylist[min_idx]:
            # min = mylist[i]
            min_idx = i

    print("found", mylist[min_idx], "at", min_idx)

    # swap(mylist, pos, min_idx)
    temp = mylist[pos]
    mylist[pos] = mylist[min_idx]
    mylist[min_idx] = temp

    print("after", pos, "step", mylist)
    pos += 1
