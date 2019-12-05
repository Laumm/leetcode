# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 =l1
        n2 = l2
        head =ListNode(0)
        bn=head
        while n1 and n2 :
            if n2.val < n1.val :
                bn.next = n2
                n2 = n2.next
            else :
                bn.next = n1
                n1 = n1.next
            bn = bn.next
        if n1 == None : bn.next = n2
        if n2 ==None : bn.next = n1
        return head.next

        

        
