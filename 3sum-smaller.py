'''
Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
'''
# Time:  O(n^2)
# Space: O(1)


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:  # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    # 如果这个和小于目标数，那就有right - left个有效的结果。
                    # 为什么呢？因为假设我们此时固定好外层的那个数，还有头指针left指向的数不变，
                    # 那把尾指针向左移0位一直到左移到left之前一位，这些组合都是小于目标数的。
                    i += 1
            k += 1

        return count
