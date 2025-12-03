mylist = [95, 82, 61, 12, 22, 32, 45, 72, 56]

def find_min_in_sublist(the_list, left, right):
    min_idx = left

    for i in range(left + 1 , right):
        if the_list[i] < the_list[min_idx]:
            min_idx = i
    return min_idx

print(find_min_in_sublist(mylist, 0, 3))
# exit()

def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp

def selection_sort(the_list):
    pos = 0

    while pos < len(mylist) - 1:
        min_idx = find_min_in_sublist(mylist, pos, len(mylist))
        print("found", mylist[min_idx], "at", min_idx)

        swap(mylist, pos, min_idx)

        print("after", pos, "swap", mylist)
        pos += 1

    return the_list

selection_sort(mylist)
print("sorted:", mylist)
# print("done", mylist)