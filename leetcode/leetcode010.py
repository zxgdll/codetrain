#!/usr/bin/env python
# coding=utf-8
# dp algorithm


class Solution(object):
    """docstring for Solution"""

    def isMatch(self, s, p):
        lens, lenp = len(s), len(p)
        dp = [[False] * (lenp + 1) for x in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, lenp + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, lens + 1):
            for j in range(1, lenp + 1):
                dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j]) if p[j - 1] == '*' \
                    else dp[i - 1][j - 1] and p[j - 1] in ('.', s[i - 1])
    return dp[lenS][lenP]
