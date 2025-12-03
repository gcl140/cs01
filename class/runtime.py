def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1


# linear search is big theta(n) of 1

# linear search
# i = 0: c1
# while loop: c2n
# total: c1 + c2n


# recursive binary search

# n = 16:
# c1 to check base case and subdivide
# n = 8
# c1 to check base case and subdivide
# n = 4
# c1 to check base case and subdivide
# n = 2
# c1 to check base case and subdivide
# n = 1
# c1 to check base case and subdivide

# n = 16 --> 8 --> 4 --> 2 --> 1
# each step costs c1
# total: c1 (log2 n + 1), simplify big theta(log2 n)

# 1+2+3+4+5+6+7+8+9+10
# sum of first n natural numbers = n(n+1)/2
# n^2 + n
# big theta(n^2)

# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):                          # looks for n, then n - 1, n -3, ....., 1 items: so runtime c1(n + n-1 + n-2 + ... + 1) = c1(n(n-1)/2) = big theta(n^2)
        min_idx = i
        for j in range(i, n):                 
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# insertion sort, best case runs once the loop , runs all, big theta(n^2)

#merge sort, mergesort(n):
# merge_sort(left n/2):  also recursive
# merge_sort(right n/2): costs c1
# combine: (left, right): costs c1
# checks just the first elements of each half, so linear time costs c2n

# ms = 16 --> ms8, (c(16)) ,ms8 -->  ms4, (c(8)) ,ms4 (for each of the two halves) --> ms2 (c(4)), ms2 (for each of the four halves) --> ms1 (c(2)) (for each of the eight halves)
# has 5 layers: c2(log2 n + 1) = big theta(n log n)

# for ns, for c16, its n, for c8, its n/2 * 2, for c4, its n/4 * 4, for c2, its n/2 * 8, for c1, its n * 16

# so big theta(n log n) - much better

# selection < insertion < merge