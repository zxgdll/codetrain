class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for x in range(len(s)):
            a = ''
            for y in range(x, len(s)):
                a += s[y]
                if a == a[::-1]:
                    d[a] = len(a)
                else:
                    d[a] = -1
        return list(item[0] for item in d.items() if item[1] == max(d.values()))[0]
a = Solution()
b = a.longestPalindrome('babad')
print(b)
