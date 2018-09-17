'''
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, i, min_diff, result = sorted(nums), 0, float("inf"), float("inf")

        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target
            i += 1

        return result


so = Solution()
print(so.threeSumClosest([0,2,1,-3], 1))


