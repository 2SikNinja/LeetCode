#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
	def getConcatenation(self, nums: List[int]) -> List[int]:
		ans = []
		for i in range(2):
			for n in nums:
				ans.append(n)
		return ans




# @lc code=end