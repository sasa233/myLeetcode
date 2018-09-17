'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rs, f = 0, ""
        if x < -231 or x > 231 - 1:
            return 0
        if x < 0:
            return -self.reverse(-x)

        while x:
            x, val = divmod(x, 10)
            rs = val + rs * 10

        return rs if rs <= 0x7fffffff else 0

    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)

if __name__ == "__main__":
    print(Solution().reverse(-230))
    print(Solution().reverse1(-910000))

