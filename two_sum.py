# link to problem: https://leetcode.com/problems/two-sum/


class Solution:
  def twoSum(self, nums, target):
    dictionary = {}

    for index, value in enumerate(nums):
      complement = target - value
      if complement in dictionary:
        return([dictionary[complement], index])
      if value not in dictionary:
        dictionary[value] = index

    return []


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
