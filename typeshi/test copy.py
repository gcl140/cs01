# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        new = []
        i = 0
        # j = len(head) - 1
        len_head = 0
        node = head
        while node:
            len_head += 1
            node = node.next

        j = len_head - 1
        
        while i < j:
            # new.append((head[i], head[j]))
            new.append(head[i])
            new.append(head[j])
            i += 1
            j -= 1
        if len(head) % 2 != 0 and i == j:
            new.append(head[i])
