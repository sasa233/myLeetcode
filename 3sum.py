'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1

        return result

so = Solution()
print(so.threeSum([-1,0,1,2,-1,-4]))



'''
# 如下方法超时了
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, target):
            mydict = {}
            valueList = []
            for index_i, value_i in enumerate(nums):
                value_j = target - value_i
                if value_j not in mydict:
                    mydict[value_i] = index_i
                else:
                    index_j = mydict[value_j]
                    valueList.append([0 - target, nums[index_j], nums[index_i]])
            return valueList

        results = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            target = 0 - nums[i]
            temp = twoSum(nums[i+1:], target)
            for i in range(0, len(temp)):
                print(temp[i])
                if temp[i] and temp[i] not in results:
                    results.append(temp[i])
        return results
'''

