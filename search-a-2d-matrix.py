'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        result = False
        if matrix == [[]] or matrix == []:
            return result

        arrayCol = [a[0] for a in matrix]
        left, right = self.binarySearch(arrayCol, target)
        if left != right and left >= 0 and right <= len(matrix):
            left, right = self.binarySearch(matrix[left], target)
        if left == right:
            result = True

        return result

    def binarySearch(self, nums, target):
        if nums == []:
            return 0, 0
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid, mid
        return left - 1, right + 1

    def searchMatrix1(self, matrix, target): # 此方法速度更快，是因为少了两次函数调用么？
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        # 可对二维数组中所有元素做二分查找，因为从左到右从上到下元素顺序排列
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // n][mid % n] >= target:
                right = mid
            else:
                left = mid + 1

        return left < m * n and matrix[left // n][left % n] == target

#print(Solution().binarySearch([1, 10, 23], 25))
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(Solution().searchMatrix(matrix, 50))
print(Solution().searchMatrix1(matrix, 50))