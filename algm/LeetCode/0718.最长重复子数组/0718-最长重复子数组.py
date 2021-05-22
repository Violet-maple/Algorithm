class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # dp[i][j] represents A[:i + 1], B[:j + 1] longest common subarray length
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        res = 0

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    res = max(dp[i][j], res)
        # print dp
        return res


def pack1(w, v, c):  # 每个东西只能选择一次
    dp = [[0 for _ in range(c + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:  # 如果剩余容量不够新来的物体 直接等于之前的
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
    return dp[len(w)][c]


def pack2(w, v, c):
    # 它是先得到第一行的值，存到dp中，然后再直接用dp相当于就是上一行的值，所以下面必须用逆序
    # 否则dp[j-w[i-1]]可能会用到你本行的值，从大到小就不会
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in reversed(range(1, c + 1)):  # 这里必须用逆序
            if w[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[c]


def pack3(w, v, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in (range(1, c + 1)):
            if w[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[c]


if __name__ == '__main__':
    # p = Solution().findLength([1, 2, 3, 2, 3, 76, 94], [2, 2, 3, 23, 54, 94])
    # print(p)
    p = pack1([2, 3, 4, 5], [3, 4, 5, 6], 8)
    print(p)
    p = pack2([2, 3, 4, 5], [3, 4, 5, 6], 8)
    print(p)
    p = pack3([2, 3, 4, 5], [3, 4, 5, 6], 8)
    print(p)
