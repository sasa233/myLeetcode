'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order,
your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        lookup, results = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]
        for digit in reversed(digits): # 倒序遍历，先放最右边/最底层的字符
            choices = lookup[int(digit)]
            m, n = len(choices), len(results)
            results += [results[i % n] for i in range(n, m * n)]
            # 将现有的results复制len(choices)份，为将choices中字符/左边字符/上一层字符放入做准备

            for i in range(0, m * n):
                results[i] = choices[i // n] + results[i]
                # choices中字符放入对应位置，每个字符作为下一层对应字符的父字符

        return results


    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 使用递归方法，从上到下遍历所有可能情况
        if not digits:
            return []
        lookup, results = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecu(results, digits, lookup, "", 0)
        return results

    def letterCombinationsRecu(self, results, digits, lookup, cur, n):
        if n == len(digits):
            results.append(cur)
        else:
            for choice in lookup[int(digits[n])]:
                self.letterCombinationsRecu(results, digits, lookup, cur + choice, n + 1)


#print(Solution().letterCombinations("234"))
print(Solution().letterCombinations1("234"))