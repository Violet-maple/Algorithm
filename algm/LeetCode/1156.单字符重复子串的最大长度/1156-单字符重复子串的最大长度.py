# coding: utf-8

from collections import Counter


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        if len(text) == text.count(text[0]):
            return len(text)
        record = Counter(text)
        start, end = 0, 1
        cur, nxt, idx_nxt = text[0], None, 0
        res = 1
        while end < len(text):
            if text[end] != cur:
                if nxt is None:
                    nxt = text[end]  # �ҵ��˵�һ�����ַ�
                    idx_nxt = end
                else:  # ��ǰ���Ѿ����
                    sub = end - 1 - start + 1  # �������һ�����ַ���ͬ�ַ��Ӵ�����
                    if sub <= record[text[start]]:  # �ж��ͬ�ַ����԰���������м��ͬ�ַ�����
                        res = max(res, sub)
                    else:
                        res = max(res, sub - 1)  # ֻ����Ŀǰ�ִ��ı߽�ͬ�ַ������ַ�����

                    cur = nxt
                    nxt = None
                    start, end = idx_nxt, idx_nxt
                    idx_nxt = 0
            if end == len(text) - 1:  # �������յ���
                # print end
                sub = end - start + 1  # �������һ�����ַ���ͬ�ַ��Ӵ�����
                # print l
                if sub <= record[text[start]]:  # �ж��ͬ�ַ����԰���������м��ͬ�ַ�����
                    res = max(res, sub)
                else:
                    res = max(res, sub - 1)  # ֻ����Ŀǰ�ִ��ı߽�ͬ�ַ������ַ�����

            # print text[start:end + 1]
            end += 1
            # print end
        return res
