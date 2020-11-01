"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2


示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000


示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000


示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 
提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

from heapq import *


class DoubleHeap(object):
    def __init__(self):
        self.maxh = []
        self.minh = []
        heapify(self.maxh)
        heapify(self.minh)
    
    def insert(self, val):
        heappush(self.minh, val)
        heappush(self.maxh, -heappop(self.minh))
        if len(self.maxh) > len(self.minh):
            heappush(self.minh, -heappop(self.maxh))
    
    def findMedian(self):
        if len(self.maxh) == len(self.minh):
            return (self.minh[0] - self.maxh[0]) / 2.0
        return self.minh[0] / 1.0


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        dh = DoubleHeap()
        for num in nums1:
            dh.insert(num)
        
        for num in nums2:
            dh.insert(num)
        
        return dh.findMedian()


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,2], [3,4]))