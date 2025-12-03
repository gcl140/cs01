# def isAnagram( s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     counts, countt = {}, {}
#     for i in range(len(s)):
#         counts[s[i]] = 1 + counts.get(s[i], 0)
#         countt[t[i]] = 1 + countt.get(t[i], 0)
#     for c in counts:
#         if counts[c] != countt[c]:
#             return False
#     print(counts)
#     print(countt)
#     return True

# # print(isAnagram("carrace", "racecar"))

def func1(n, m):
    i = 0
    while i < n:
        j = i
        while j < m:
            print(i, j)
            j = j + 1
        i = i + 1

# func1(2, 3)

def func2(glist):
    i = 1
    temp = glist[0]
    while i < len(glist):
        glist[i - 1] = glist[i]
        i = i + 1
    glist[len(glist) - 1] = temp

alist = [6, 2, 4, 7]
func2(alist)
# print(alist)

def func3(glist):
    x = len(glist[0])
    for s in glist:
        if x < len(s):
            x = len(s)
    return x
# print(func3(["exam", "mango", "fun"]))

def func4(glist):
    for ele in glist:
        if ele >= 0:
            return "a"
        else:
            return "b"
        
# print(func4([-4, 5, 10]))

meaning = ["f", "o", "r", "t", "y", "t", "w", "o"]
for value in meaning:
    value ="cs1"

# print(meaning)