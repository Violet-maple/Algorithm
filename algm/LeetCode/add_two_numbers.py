# coding: utf-8
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
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
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        l3 = temp
        a = 0
        # 当l1不为空或者l2不为空或者a不等于0的时候
        while l1 or l2 or a != 0:
            if l1:
                # a等于a加上l1当前的值
                a += l1.val
                # l1的指针指向下一个
                l1 = l1.next
            if l2:
                a += l2.val
                l2 = l2.next
                # temp的下一个的值就是 a%10
            temp.next = ListNode(a % 10)
            temp = temp.next
            a = a // 10
        # l3代替temp来输出链表
        return l3.next


if __name__ == '__main__':
    listNode1 = ListNode(2)
    listNode1.next = ListNode(4)
    listNode1.next.next = ListNode(3)
    
    listNode2 = ListNode(5)
    listNode2.next = ListNode(6)
    listNode2.next.next = ListNode(4)
    ret = Solution().addTwoNumbers(listNode1, listNode2)
    print(ret.value)
