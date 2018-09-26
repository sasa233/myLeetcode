'''
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if matrix == []:
            return result

        left, right, top, buttom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= buttom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for j in range(top + 1, buttom):
                result.append(matrix[j][right])
            for i in reversed(range(left, right + 1)):
                if top < buttom:
                    result.append(matrix[buttom][i])
            for j in reversed(range(top + 1, buttom)):
                if left < right:
                    result.append(matrix[j][left])
            left, right, top, buttom = left + 1, right - 1, top + 1, buttom - 1
        return result

print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))

