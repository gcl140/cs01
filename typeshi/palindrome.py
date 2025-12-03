# def isPalindrome( s: str) -> bool:
#     new = []
#     for i in range(len(s)):
#         new.append(s[i])

#     arranged = set(new)
#     new.reverse()
#     arranged_reverse = set(new)
#     return arranged == arranged_reverse

# def isPalindrome( s: str) -> bool:
#     s = list(s)
#     arranged = set(s)
#     s.reverse()
#     arranged_reverse = set(s)
#     print(arranged)
#     print(arranged_reverse)
#     return arranged == arranged_reverse    

def isPalindrome( s: str) -> bool:
    new = []
    s = list(s)
    for i in range(len(s)):
        print(s[i], i)
        new.append(s[i].lower())
    og = new
    new.reverse()
    reversedd = new 
    return og == reversedd


# def isPalindrome( s: str) -> bool:
#     s = list(s)
#     new = []
#     for i in range(len(s)):
#         if s[i] != " ":
#             s[i] = s[i].lower()
#             new.append(s[i])        

#     before = new
#     new.reverse()
#     later = new

#     return before == later

print(isPalindrome("race a car"))
            

# def isPalindrome( s: str) -> bool:
#     # stripped = s.strip()
#     new = []
#     for i in range(len(s)):
#         # if s[i] != " ":
#             # stripped.remove(s[i])
#             print(s[i])
#             new.append(s[i])

#     arranged = set(new)
#     new.reverse()
#     arranged_reverse = set(new)
#     # arranged_reverse = set(new.reverse())
#     return arranged == arranged_reverse
    

# print(isPalindrome("A man a plan a canal Panama"))  # True
# print(isPalindrome("A man a plan a canal Panama"))  # True
# print(isPalindrome("racecar"))  # True
# print(isPalindrome("hello"))    # False

# def revas(lst):
#     new_lst = []
#     # for i in range(len(lst) - 1, -1, -1):
#     #     new_lst.append(lst[i])
#     # return new_lst
#     new_lst = lst.reverse()
#     return new_lst


# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)

# print(revas([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]