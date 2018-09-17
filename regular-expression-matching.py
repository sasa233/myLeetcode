class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        result[0][0] = True

        for j in range(2, len(p) + 1):    #从2开始，别让result[0][j - 2]数组溢出
            if p[j - 1] == "*":
                result[0][j] = result[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != "*":
                    result[i][j] = result[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                else:
                    result[i][j] = result[i][j - 2] or (result[i - 1][j] and (s[i - 1] == p[j - 1 - 1] or p[j - 1 - 1] == "."))
                    # 1、"*"匹配0次：
                    # 因"*"前必有字符，则result[i][j - 2]不会出现result[i][1 - 2]的情况，j - 1 > 0, j > 1
                    #
                    # 2、"*"匹配1次或多次：
                    # s[i - 1] == p[j - 1 - 1] or p[j - 1 - 1] == "." 中,
                    # p[j - 1 - 1]意味着用p当前字符的前一个字符(p[j - 1 - 1])(也就是"*"对应的字符)与s中当前字符(s[i - 1])比较；
                    # 将之前dp结果result[i - 1][j]也考虑进来

        return result[len(s)][len(p)]

print(Solution().isMatch("abab", "a*b*"))

# result[i][j - 2] *匹配前面字符0次
# result[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')  *匹配前面字符1次或多次