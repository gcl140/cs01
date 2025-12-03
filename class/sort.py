mylist = [11, 0, 35, 16, 53, 141, -2, 31, 26, 45]

# mylist.sort()

new = []
print(new)
smallest = mylist[0]
# new.append(mylist[0])

for i in range(len(mylist)):
    # for j in range(i + 1, len(mylist)):
    if mylist[i] <= smallest:
        min_idx = i
        smallest = mylist[i]
        print(smallest)
        mylist.remove(smallest)
        new.append(smallest)

# print(mylist)
# print(new)
# print("found ", smallest, "min at ", min_idx)
