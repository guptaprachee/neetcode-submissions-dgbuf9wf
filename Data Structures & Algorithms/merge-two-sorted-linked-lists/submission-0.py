# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currptr= dummy
        while list1 and list2:
            if list1.val< list2.val:
                currptr.next = list1
                list1 =list1.next
            else:
                currptr.next =list2
                list2=list2.next
            currptr = currptr.next

        if list1:
            currptr.next = list1
        elif list2:
            currptr.next = list2
            
        return dummy.next

            

      
                
        
        