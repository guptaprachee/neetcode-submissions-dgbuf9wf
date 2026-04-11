# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l, r = None, head
        while r:
            temp = r.next
            r.next =l
            l=r
            r= temp

        
        return l
            

        