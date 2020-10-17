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


class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()  # 记录每个字母最后一次出现的下标,key是字母，val是下标
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:  # 出现过
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end  # 刷新最新下标
            res = max(res, end - start + 1)  # 刷新res
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))
