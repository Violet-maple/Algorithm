"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 第一种思路：双重循环暴力解:
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        for index, item in enumerate(nums):
            for count in range(index + 1, len(nums)):
                if item + nums[count] == target:
                    return [index, count]


## 第二种思路：用hash map记录之前出现的数字及下标，key是数字，val是下标。
class Solution2(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, item in enumerate(nums):
            if target - item in hash_map:
                return [hash_map[target - item], index]
            hash_map[item] = index


if __name__ == '__main__':
    print(Solution2().twoSum([2, 7, 11, 15], 9))
