'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step, zigzag = 2 * numRows - 2, ""
        # 确定每行的字符，一行一行来
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j] #这是第一行和最后一行
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
                    # j + step - 从当前字符开始向上走，到步长处为止的步数 - 走到j位置所用的步数
                    # j + step - i - i，也就是 j + step - 2 * i
                    # 当然 j + step - 2 * i需小于字符串长度
        return zigzag

if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
