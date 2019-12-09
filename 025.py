class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k: int) :
        if k == 1 :
            return head
        node = head
        nodes = []
        num = 0
        while node :
            num += 1
            nodes.append(node)
            node = node.next
            if num  ==  k  :
                break
        if num < k  :
            return head
        for i in range(k-1):
            nodes[k-i-1].next = nodes[k-i-2]
        nodes[0].next = self.reverseKGroup(node,k)
        return  nodes[-1]
            



