

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.

def binary_search(the_list, key, left = None, right = None):
    # If using the default parameters, then search the entire list.
        if left == None and right == None:
            left = 0
            right = len(the_list) - 1

        # YOU FILL IN THE REST OF THIS FUNCTION.
        
        if left > right or len(the_list) == 0:
              return None

        mid = (left + right) // 2

        if key == the_list[mid]:
              return mid
        if the_list[mid] < key:
              return binary_search(the_list, key, mid + 1, right)
        else:
              return binary_search(the_list, key, left, mid - 1)

# print(binary_search([23, 45, 7, 38, 29, 39, 3, 5, 7, 8, 4, 36, 55, 9, 90, 34], 5))
print(binary_search([27, 78, 105, 135, 411, 431, 434, 468, 493, 501, 525, 534, 551, 654, 780], 5))
# print(binary_search([27, 78, 105, 135, 411, 431, 434, 468, 493, 501, 525, 534, 551, 654, 780], 135, 2, 12))
# print(binary_search([], 135, 2, 12))
