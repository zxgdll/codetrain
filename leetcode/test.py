# a = [1, 3, 2, 5, 4, 1]
# b = a.index(1)
# print(b)
# a[b] = 'a'
# print(a.index(1))
# a1 = 123
# a1 /= 10
# print(a1)
# s = 'abcabcbb'
# b = {}
# for x in range(len(s) - 1):
#     a = ''
#     for y in range(x, len(s)):
#         if s[y] not in a:
#             a += s[y]
#         else:
#             break
#     b[a] = len(a)
# print(b)
# print(max(b.values()))
# b = {}
# if b:
#     print(True)
# dic = {}
# a = ()
# for x in range(len(s)):


class Solution(object):
    """docstring for Solution"""

    def lengthOfLongestSubstring(self, s):
        res = 0
        lef = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= lef:
                lef = d[ch] + 1
            d[ch] = i
            res = max(res, i - lef + 1)
        return res
