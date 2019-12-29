# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head : return head
        n = 0
        node = head
        tail = None 
        while node :
            n += 1
            tail = node
            node = node.next
        move = k % n
        if move == 0 : return head
        node = head
        i = 0
        while node :
            i += 1
            if i + move ==   n : 
                new_head = node.next
                node.next = None 
                tail.next = head
                break
            node = node.next
        return new_head
