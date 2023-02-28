class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()

        p = list1
        q = list2
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.val <= q.val:
                s = p 
                p = s.next 

            else:
                s = q
                q = s.next 
            new_head = s

        while p and q: 
            if p.val < q.val:
                s.next = p 
                s = p 
                p = s.next 
            else: 
                s.next = q
                s = q 
                q = s.next 
        if not p: 
            s.next = q
        if not q:
            s.next = p 

        self.head = new_head 
        return self.head
