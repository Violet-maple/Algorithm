class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right-left) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                # print nums[left]
                return mid
        return -1


if __name__ == '__main__':
    p = Solution().search([2, 2, 4, 7, 8], 4)
    print(p)
