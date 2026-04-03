class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Calculate length
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        # Step 2: If removing head
        if n == length:
            return head.next
        
        # Step 3: Move to node before target
        ptr = head
        for _ in range(length - n - 1):
            ptr = ptr.next
        
        # Step 4: Remove node
        ptr.next = ptr.next.next
        
        return head