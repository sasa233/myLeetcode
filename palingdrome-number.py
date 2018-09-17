class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        copy, reverse = x, 0
        while copy:
            reverse = reverse * 10 + copy % 10
            copy = copy // 10

        return x == reverse

print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12320))
print(Solution().isPalindrome(-12321))

