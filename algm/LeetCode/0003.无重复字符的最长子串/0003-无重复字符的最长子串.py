# coding: utf-8

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是
"abc"，所以其
长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是
"b"
，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是
"wke"
，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，
"pwke"
 是一个子序列，不是子串。
思路：

问子串可以考虑用双指针法 +  sliding window解题，start， end可以夹出一个window。

用end线性遍历每个数组，用record记录下每个字母出现的最新的下标。

当遇到一个新元素char在record里没有记录时，代表它没有跟window里的字母重复。

如果在record里有记录，说明start需要刷新， 取当前start和record[char]里的最大值作为新的start即可。
"""
import random
import string


# 方法1 最优解
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = temp = ''
        for char in s:
            if char in temp:
                temp = temp[temp.index(char) + 1:]
            temp += char
            if len(temp) > len(ans):
                ans = temp
        return len(ans)


# 方法2 （两次 Max耗时）


class Solution1(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end
            res = max(res, end - start + 1)
        return res


# 方式3 效率高一点点
class Solution2:
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 存储历史循环中最长的子串长度
        max_len = 0
        # 判断传入的字符串是否为空
        if s is None or len(s) == 0:
            return max_len
        # 定义一个字典，存储不重复的字符和字符所在的下标
        str_dict = {}
        # 存储每次循环中最长的子串长度
        # one_max = 0
        # 记录最近重复字符所在的位置+1
        start = 0
        for i in range(len(s)):
            # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
            if s[i] in str_dict and str_dict[s[i]] >= start:
                # 记录当前字符的值+1
                start = str_dict[s[i]]
            # 在此次循环中，最大的不重复子串的长度
            one_max = i - start + 1
            # 把当前位置覆盖字典中的位置
            str_dict[s[i]] = i
            # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
            max_len = max(max_len, one_max)
        return max_len - 1


if __name__ == '__main__':
    value = ''.join((random.choice(string.ascii_letters) for _ in range(100000)))
    print('ok')
    print(Solution().lengthOfLongestSubstring(value))
    print(Solution1().lengthOfLongestSubstring(value))
    print(Solution2().lengthOfLongestSubstring(value))
