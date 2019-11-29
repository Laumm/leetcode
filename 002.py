# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1  = l1
        n2  = l2
        base = 0
        while True :
            total = n1.val + n2.val + base
            base = total // 10
            n1.val= total % 10
            
            if n1.next is None :
                n1.next = n2.next
                n2.next= None
            if n1.next is None :
                if base == 0:
                    break
                else :
                    n1.next = ListNode(0)
                    n1= n1.next
                    n2.next = ListNode(0)
                    n2 = n2.next
                    continue
            
            if n2.next is None:
                if base == 0 :
                    break
                else :
                    n1 =n1.next
                    n2.next = ListNode(0)
                    n2 = n2.next
                    continue
            n1= n1.next
            n2 = n2.next
        return l1
