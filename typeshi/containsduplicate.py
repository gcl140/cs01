# class Solution:
def hasDuplicate(nums):
    new = []
    for no in nums:
        if not no in new:
            new.append(no)
        else:
            return True
    return False

print(hasDuplicate([1, 2, 4, 3]))


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         new = []
#         for no in nums:
#             if not no in new:
#                 new.append(no)
#             else:
#                 return True
#         return False