# Definition for singly-linked list.
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @property
    def value(self):
        val = self.val
        node = self.next
        i = 1
        while node:
            val += node.val * 10 ** i
            node = node.next
            i += 1
        return val


class Solution(object):
    
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        temp = node
        val = 0
        # 当l1不为空或者l2不为空或者a不等于0的时候
        while l1 or l2 or val:
            val, cur = divmod(val + (l1.val if l1 else 0) + l2.val if l2 else 0, 10)
            temp.next = ListNode(cur)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return node.next
    
    @staticmethod
    def generateList(l: list) -> ListNode:
        node = ListNode(0)
        temp = node
        for val in l:
            temp.next = ListNode(val)
            temp = temp.next
        return node.next
    
    @staticmethod
    def printList(l: ListNode):
        while l:
            print("%d, " % l.val, end='')
            l = l.next
        print('')


class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getLength(l1) < self.getLength(l2):
            l1, l2 = l2, l1
        head = l1
        while l2:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        
        p = head
        while p:
            if p.val > 9:
                p.val -= 10
                if p.next:
                    p.next.val += 1
                else:
                    p.next = ListNode(1)
            p = p.next
        return head
    
    @staticmethod
    def getLength(l):
        tmp = 0
        while l:
            tmp += 1
            l = l.next
        return tmp


if __name__ == '__main__':
    listNode1 = Solution.generateList([2, 4, 3])
    listNode2 = Solution.generateList([5, 6, 4])
    ret = Solution().addTwoNumbers(listNode1, listNode2)
    print(ret.value)
