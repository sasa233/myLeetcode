'''
Given a positive integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result, num = [], 1
        if n == 0:
            return result

        matrix = [[0 for _ in range(0, n)] for _ in range(0, n)]
        left, right, top, buttom = 0, n - 1, 0, n - 1
        while left <= right and top <= buttom:
            for i in range(left, right + 1):    # 此处包含了n为奇数时，left等于right的情况
                matrix[top][i] = num
                num += 1
            for j in range(top + 1, buttom):    # 此处包含了n为奇数时，top等于buttom的情况
                matrix[j][right] = num
                num += 1
            for i in reversed(range(left, right + 1)):
                if top < buttom:
                    matrix[buttom][i] = num
                    num += 1
            for j in reversed(range(top + 1, buttom)):
                if left < right:
                    matrix[j][left] = num
                    num += 1
            left, right, top, buttom = left + 1, right - 1, top + 1, buttom - 1
        return matrix

print(Solution().generateMatrix(3))