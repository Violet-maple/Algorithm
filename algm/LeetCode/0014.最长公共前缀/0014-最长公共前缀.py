"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"


示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        
        res = ""
        pair = zip(strs[0], strs[-1])
        for x, y in pair:
            if x == y:
                res += x
            else:
                break
        return res
    
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                res += tmp[0]
            else:
                break
        return res


if __name__ == '__main__':
    print(Solution().longestCommonPrefix1(["flowerl", "fowhlj", "flight"]))
