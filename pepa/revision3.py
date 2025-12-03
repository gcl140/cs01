# def reverse(s):
#     # you write this part
#     if s == "":
#         return ""
#     head = s[0]
#     rest = s[1:]
#     return "" + reverse(rest) + head

# print("Reverse: ",reverse("ward"))

# # Compute n! recursively.
# def factorial(n):
#     # you write this part
    
#     if n == 0:
#         return 1
#     return factorial(n -1) * n

# print("Factorial: ",factorial(5))

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print("Fibonacci: ",fibonacci(5))

# def binary_search(alist, target, left=None, right=None):
    
#     if left == None and right == None:
#         left = 0
#         right = len(alist) - 1


#     if len(alist) == 0 or left > right:
#         return None
    
#     mid = (left + right) // 2
#     if alist[mid] == target:
#         return mid
    
#     if alist[mid] < target:
#         return binary_search(alist, target, mid + 1, right)
#     else:
#         return binary_search(alist, target, left, mid - 1)
    
# # the_list = [5,6,15,7,78,3,4,0, 5]
# # the_list.sort()
# # print(the_list)
# # print(binary_search(the_list, 7))

# def binary_no_rec_search(alist, target):
#     left = 0
#     right = len(alist) - 1
#     while left <= right:
#         mid = (left + right)//2
#         if alist[mid] == target:
#             return mid
#         elif alist[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return None

# the_list = [5,6,15,7,78,3,4,0, 5]
# the_list.sort()
# print(the_list)
# print(binary_no_rec_search(the_list, 7))

# Define a recursive function that takes a positive integer
# n as a parameter and prints the squares of all the number
# s between 1 and n in decreasing order.

# def functionn(n):
#     if n < 0:
#         return "not positive"
#     if n == 0:
#         # return print("0")
#         print("0")
#     else:
#         print(n**2)
#         functionn(n - 1)
    
# functionn(6)

# Define a recursive function that takes a positive integer 
# n as a parameter and prints the squares of all the numbers
# between 1 and n in increasing order.

# def functionn(n):
#     if n < 0:
#         return "not positive"
#     functionn(n - 1)
#     print(n**2)
    
    
# functionn(6)

# Define a recursive function that takes a positive integer 
# n as a parameter and prints the squares of all the even 
# numbers between 1 and n in increasing order.

# def functionn(n):
#     if n < 0:
#         return
#     functionn(n - 1)
#     if n % 2 == 0:
#         print(n ** 2)

# functionn(6)

# Define a recursive function that takes a positive integer 
# n as a parameter and returns the product of all the odd 
# numbers between 1 and n.

# def functionn(n):
#     if n < 0:
#         return 
#     if n == 1:
#         return 1
#     elif n % 2 != 0:
#         return n * functionn(n - 1)
#     else:
#         return functionn(n - 1)
    
# print(functionn(9))

# Define a recursive function that takes two positive 
# integers n and p as parameters and returns a list of all 
# multiples of p between 1 and n. The order of numbers in 
# the returned list doesn't matter.

# def functionn(n, p):
#     if p < 0 or n < 0:
#         return
#     if n == 1:
#         if n % p == 0:
#             return [1]
#         else:
#             return []
#     if n % p == 0:
#         return [n] + functionn(n - 1, p)
#     else:
#         return functionn(n - 1, p)


# def functionn(n, p):
#     if p < 0 or n < 0:
#         return
#     if n == 0:
#         return []
#     if n % p == 0:
#         return [n] + functionn(n - 1, p)
#     else:
#         return functionn(n - 1, p)

# print(functionn(9, 3))

# Define a recursive function that takes a list of positive 
# integers, glist, as a parameter and returns a list of all 
# multiples of 3 in glist.

# def func(alist, i):
#     if len(alist) == 0:
#         return []
    
#     head = alist[0]
#     rest = alist[1:]

#     if head % i == 0:
#         return [head] + func(rest, i)
#     else:
#         return func(rest, i)
    
# print(func([1,2,3,4,5,6,7,8,9,0], 3))

# Define a recursive function that takes a list of positive 
# integers, glist, as a parameter and returns True if the 
# list has a multiple of 3. Otherwise, it returns False.

# def func(alist, p):
#     if len(alist) == 0:
#         return
#     head = alist[0]
#     rest = alist[1:]

#     if head % p == 0:
#         return True
#     else:
#         return func(rest, p)
    
# print(func([1,2,3,4,5,6,7,8,9,0], 3))


# Fibonnacci
# def fibo(idx):
#     if idx <= 1:
#         return idx
#     return fibo(idx - 1) + fibo(idx - 2)

# # 5 - 4 + 3 - 3 + 1 - 


# w = [0,1,1,2,3,5,8,13,21,34]
# print(fibo(3 ))


# def fibo(idx):
#     seq = [0, 1]
#     for i in range(idx):
#         seq.append(seq[-1] + seq[-2])
#     return seq[-2]
# print(fibo(3))


def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist

def selection_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(i, len(alist)):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

def insertion_sort(alist):
    for i in range(1, len(alist)):
        j = i - 1
        key = alist[i]
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key
    return alist


w = [0,1,1,2,8,5,13,21,34,3]
# print(bubble_sort(w))
# print(selection_sort(w))
print(insertion_sort(w))
