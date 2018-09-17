'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

#使用manacher算法

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ["^","$"]
            T = ["^"]
            for c in s:
                T += ["#", c]
            T += ["#", "$"]
            return T

        T = preProcess(s)
        l = len(T)
        P = [0] * l
        center, right = 0, 0
        for i in range(1, l - 1):
            i_mirror = center * 2 - i
            if i < right:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in range(1, l):
            if P[i] > P[max_i]:
                max_i = i
        start_i = (max_i - 1 - P[max_i]) // 2   #找到对应在s中的开始index
        return s[start_i : start_i + P[max_i]]

#print(Solution().longestPalindrome("babcbabcbaccba"))
print(Solution().longestPalindrome("cbcbbb"))