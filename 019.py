# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        initNode = ListNode(0)
        initNode.next=head
        record = [initNode]
        node = head
        while node :
            record.append(node)
            node= node.next
        record[-n-1].next=record[-n].next
        return initNode.next
