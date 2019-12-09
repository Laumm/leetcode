# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0 :
            return None
        if n == 1 :
            return lists[0]
        left = self.mergeKLists(lists[:n//2])
        right = self.mergeKLists(lists[n//2:])
        baseNode = ListNode(None)
        baseNode.next = left
        middNode =baseNode
        while left and right :
            if right.val < left.val :
                middNode.next = right
                right = right.next
            else:
                middNode.next = left
                left = left.next
            middNode = middNode.next
        if left == None:middNode.next = right
        if right == None : middNode.next = left
        return baseNode.next
                

                


