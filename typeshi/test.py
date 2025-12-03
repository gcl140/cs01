# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         # for i in range(len(head)):
#         #     for j in range()

#         new = []
#         i = 0
#         j = len(head) - 1
#         while i < len(head):
#             new.append((head[i], head[j]))
#             i += 1
#             j -= 1


head = [1,2,3,4,5, 8]

new = []
i = 0
j = len(head) - 1
while i < j:
    # new.append((head[i], head[j]))
    new.append(head[i])
    new.append(head[j])
    i += 1
    j -= 1
if len(head) % 2 != 0 and i == j:
    new.append(head[i])

print(new)
