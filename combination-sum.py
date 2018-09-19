'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        results, candidates = [], sorted(candidates)
        #self.combinationSumRecu(candidates, target, results, [])
        self.combinationSumRecu1(candidates, target, results, [], 0)
        return results

    def combinationSumRecu(self, candidates, target, results, cur):
        if target == 0:
            cur = sorted(cur)
            if cur not in results:
                results.append(cur)
        elif target < 0:
            return
        else:
            for num in candidates:
                self.combinationSumRecu(candidates, target - num, results, cur + [num])
        # 此方法实际上对n * n的二维数组进行了遍历，其实无需这样
        # 在第一层循环中，使用过的num不应再出现在后续的遍历中

    def combinationSumRecu1(self, candidates, target, results, cur, start):
        if target == 0:
            results.append(cur)
        elif target < 0:
            return
        else:
            while start < len(candidates) and candidates[start] <= target:
                self.combinationSumRecu1(candidates, target - candidates[start],
                                         results, cur + [candidates[start]], start)
                start += 1
            # for num in candidates[start:]:
            #     self.combinationSumRecu1(candidates, target - num, results, cur + [num], start)
            #     start += 1
            # for循环这段代码速度更慢，怀疑是因为candidates[start:]的原因


print(Solution().combinationSum([2,3,5], 8))