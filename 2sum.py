'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # mydict就是用来记录已经遍历过的值
        # 后续的每一个值都是和前面已经遍历过的值进行配对，找到位置
        mydict = {}
        indexList = []
        for index_i, value_i in enumerate(nums):
            value_j = target - value_i
            if value_j not in mydict:
                mydict[value_i] = index_i
            else:
                index_j = mydict[value_j]
                indexList.extend([index_j, index_i])
        return indexList

so = Solution()
print(so.twoSum([3,2,4],6))


class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #不能考虑排序的做法，因为此题要求的必须是原始的index，排序后会失去这个信息
        for first_num in nums:
            second_num = target - first_num
            first_index = nums.index(first_num)
            second_index_start = first_index + 1
            if second_num in nums[second_index_start:]:
                second_index = second_index_start + nums[second_index_start:].index(second_num)
                return [first_index, second_index]

so1 = Solution1()
print(so1.twoSum([3,2,4],6))