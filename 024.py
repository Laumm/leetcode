# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node =head
        nodes = []
        while node :
            nodes.append(node)
            node = node.next
        for i in range(1,len(nodes),2):
            # 设置头信息
            if i >= 2 :
                nodes[i-2].next = nodes[i]
            # 交换节点
            nodes[i-1].next = nodes[i].next
            nodes[i].next = nodes[i-1]
            nodes[i-1],nodes[i] = nodes[i],nodes[i-1]

        return nodes[0] if len(nodes) >0 else None



