# link to problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
  def lengthOfLongestSubstring(self, s):
    myset = set()
    maximum = 0

    j = 0
    for i in range(len(s)):

      while s[i] in myset:
        myset.remove(s[j])
        j += 1

      myset.add(s[i])
      maximum = max(i - j + 1, maximum)

    return maximum


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))
