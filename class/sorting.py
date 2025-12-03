# simpler problem: sort a list where left and right sides are already sorted

# remember base case:
# [1], [6], []
# base case


def selection_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(i, len(alist)):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one step ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive calls
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements (if any)
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


nums = [5, 3, 8, 4, 2]

bubble_sort(nums)
print("Bubble:", nums)

nums = [5, 3, 8, 4, 2]
insertion_sort(nums)
print("Insertion:", nums)

nums = [5, 3, 8, 4, 2]
selection_sort(nums)
print("Selection:", nums)

nums = [5, 3, 8, 4, 2]
merge_sort(nums)
print("Merge:", nums)
