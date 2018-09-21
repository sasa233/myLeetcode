'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        # n是target，k是组成元素的个数
        results = []
        self.combinationSumRecu(n, results, [], 1, k) # start从1开始，1、2、3、4...8、9
        return results

    def combinationSumRecu(self, target, results, cur, start, k):
        if target == 0 and k == 0:
            results.append(cur)
        elif k < 0:
            return
        else:
            while start < 10 and start * k + k * (k - 1) / 2 <= target:
                # 如果从start开始连续三个数之和大于target，这个start就肯定不用考虑了，因为其他的三个数组合肯定更大
                # 等差数列：前n项和公式为：Sn=na1+n(n-1)d/2，（n为正整数）
                self.combinationSumRecu(target - start, results, cur + [start], start + 1, k - 1)
                start += 1

print(Solution().combinationSum3(3, 9))




