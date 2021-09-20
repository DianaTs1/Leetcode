class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        a = head
    
        while a.next:
            if a.val != a.next.val:
                a = a.next
            else:
                a.next = a.next.next     
                
        return head