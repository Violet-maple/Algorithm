class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # ʮ���ǹ������֣�Ҫ�������������
        # �˸��ǹ������֣� Ҫ���ĸ���������
        # ʮ���ǹ������֣�Ҫ�������������
        #         hashmap = dict()
        #         for c in candies:
        #             hashmap[c] = hashmap.get(c, 0) + 1

        #         cnt = len(hashmap.keys())

        return min(len(set(candies)), len(candies) // 2)
