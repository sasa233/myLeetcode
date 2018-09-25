'''
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''
class Solution:
    def combinationSum4(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        results, candidates = [], sorted(candidates)
        self.combinationSumRecu(candidates, target, results, [])
        return len(results)

    def combinationSumRecu(self, candidates, target, results, cur):
        if target == 0:
            if cur not in results:
                results.append(cur)
        elif target < 0:
            return
        else:
            for num in candidates:
                self.combinationSumRecu(candidates, target - num, results, cur + [num])
            # 将所有元素遍历一遍

    def combinationSum4_2(self, candidates, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        candidates.sort()
        for i in range(1, target + 1):
            for j in range(0, len(candidates)):
                if candidates[j] <= i:
                    dp[i] += dp[i - candidates[j]]
                else:
                    break
        return dp[target]

    # 这道题是组合之和系列的第四道，我开始想当然的一位还是用递归来解，结果写出来发现TLE了，
    # 的确OJ给了一个test case为[4,1,2] 32，这个结果是39882198，用递归需要好几秒的运算时间，实在是不高效，
    # 估计这也是为啥只让返回一个总和，而不是返回所有情况，不然机子就爆了。
    # 而这道题的真正解法应该是用DP来做，解题思想有点像之前爬梯子的那道题Climbing Stairs，
    # 我们需要一个一维数组dp，其中dp[i]表示目标数为i的解的个数，然后我们从1遍历到target，
    # 对于每一个数i，遍历nums数组，如果i>=x, dp[i] += dp[i - x]。
    # 这个也很好理解，比如说对于[1,2,3] 4，这个例子，当我们在计算dp[3]的时候，
    # 3可以拆分为1+x，而x即为dp[2]，
    # 3也可以拆分为2+x，此时x为dp[1]，
    # 3同样可以拆为3+x，此时x为dp[0]，
    # 我们把所有的情况加起来就是组成3的所有情况了。

#print(Solution().combinationSum4([4, 1, 2], 32))
print(Solution().combinationSum4_2([4, 1, 2], 32))