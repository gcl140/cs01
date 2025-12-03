def fact(n):
    if n == 1 or n == 0:    # Base case
        return 1
    return fact(n - 1) * n  # Recursive case

# print(fact(5))

fibonnachi = [1, 1, 2, 3, 5, 8, 13, 21]

# fib(0) = 1
# fib(1) = 1
# fib(2) = fib(1) + fib(0)
# fib(3) = fib(2) + fib(1)
# fib(4) = fib(3) + fib(2)
# fib(n) = fib(n - 1) + fib(n - 2)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n- 2)

# print(fib(50))

def binary_search(alist, n):
    lll = len(alist)
    if lll % 2 == 0:
        lll = lll + 1

    alist.sort()
    print(alist)
    if lll > 1:
            if alist[lll//2] == n:
                return alist[lll//2]
            if alist[lll//2] <= n:
                del alist[0: lll//2]
            else:
                return n
    else:
        return alist[0]

# print(binary_search([1, 9, 45, 3, 21, 67, 78], 45))


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n- 2)

    for i in range(n):
        return fib(n - 1) + fib(n - 2)
    print(fib(10))


# def sort(alist):
#     # small = alist[0]
#     for i in range(len(alist) - 1):
#         # for j in range(len(alist)):
#             if alist[i + 1] < alist[i]:
#                 alist[i], alist[i + 1] = alist[i + 1], alist[i]
#     return alist


def sort(alist):
    for i in range(len(alist) - 1):
        for j in range(i, len(alist)):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

# print(sort([5, 3, 8, 6, 2, 7, 4, 1]))

def insertion_sort(the_list):
    n = len(the_list)   # how many items to sort

    for i in range(1, n):
        key = the_list[i]   # remember what was in the ith position

        j = i-1     # look in positions to the left of i
        while j >= 0 and the_list[j] > key:
            the_list[j+1] = the_list[j]
            # the_list[i] = the_list[j]
            j -= 1

        the_list[j+1] = key

grade_list = [89, 45, 85, 81, 77, 94, 22, 79, 92, 91]
insertion_sort(grade_list)
print(str(grade_list))
