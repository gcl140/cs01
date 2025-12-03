groceries = ["apple", "banana", "carrot", "milk", "bread"]
# print(groceries)
groceries[1] = "strawberries"
# print(groceries[1])

aapl = [150.75, 153.31, 155.12, 154.22, 156.45]

# for i in range(len(aapl)):
#     aapl[i] = aapl[i] + 1.17

id = 1
def unyama():
    while id < len(aapl):
        aapl[id] = round(aapl[id] * 1.17, 2)
        id = id + 1

def ukoko():
    id = 0
    while id < len(aapl):
        item = aapl[id]
        print(item*2)
        id += 1

double_aapl = []
for share_price in aapl:
    double_aapl.append(share_price * 2)

del double_aapl[2]
# print(aapl)
# print(double_aapl)

mylist = ["Dartmouth", "Harvard", "Brown", "Princeton", "Columbia"]

def find_item(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            print("Found it! at index", i)
            # break
            return i
        i += 1

# find_item(mylist, "Brown")

def square(x):
    result = x * x
    x = 10
    return result

def change_value(the_list):
    the_list[3] = "Changed!"
    return the_list


#needs an address of the memory and the index of the list to be able to change the value, but only does so for lists
mylist = ["Dartmouth", "Harvard", "Brown", "Princeton", "Columbia"]
# print(change_value(mylist))

def find_strings(mylist, n):
    # i = 0
    for i in range(len(mylist)):
        if len(mylist[i]) > n:
            print(mylist[i])
    return mylist[i]

# find_strings(mylist, 7)

mystring = "The quick brown fox jumps over the lazy dog"

new_string = ""
#take every 3rd character from mystring and create a new string
i = 0
while i < len(mystring):
    new_string += mystring[i]
    i += 3

# print(new_string)

def double_list(input_list):
    # new_list = []
    i = 0
    while i < len(input_list):
        # new_list.append(input_list[i] * 2)
        input_list += [input_list[i] * 2]
        i += 1
    return input_list

# print(double_list([1,2,3,4,5]))


# def reverse_list(somelist):
#     i = 0
#     j = len(somelist) - 1
#     new = []
#     while i < j:
#         new.append(somelist[j])
#         new.append(somelist[i])
#         j = len(somelist) - 1 - i
#         i += 1
#         j -= 1

def reverse_list(somelist):
    i = 0
    j = len(somelist) - 1
    new = []
    # while i < len(somelist)//2:
    while i < j:
        # j = len(somelist) - 1 - i
        temp = somelist[i]
        somelist[i] = somelist[j]
        somelist[j] = temp
        print(i, somelist)
        i += 1
        j -= 1

    return somelist
print(reverse_list([1,2,3,4,5,9]))
