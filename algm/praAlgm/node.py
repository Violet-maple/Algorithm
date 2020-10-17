# coding: utf-8

"""
链表成对调换

1->2->3->4 转换成2->1->4->3.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

   
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        return head
    
if __name__ == '__main__':
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    listNode.next.next.next = ListNode(4)
    ret = Solution().swapPairs(listNode)
    print(ret)
