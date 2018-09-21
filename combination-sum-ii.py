'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        results, candidates = [], sorted(candidates)
        #self.combinationSumRecu(candidates, target, results, [])
        self.combinationSumRecu(candidates, target, results, [], 0)
        return results

    def combinationSumRecu(self, candidates, target, results, cur, start):
        if target == 0:
            if cur not in results:
                results.append(cur)
        else:
            while start < len(candidates) and candidates[start] <= target:
                self.combinationSumRecu(candidates, target - candidates[start],
                                         results, cur + [candidates[start]], start + 1)
                # start + 1是因为题目要求candidates中每个元素就出现一次，不再考虑上一层的元素
                start += 1

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))