# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = {}
        distance = 0
        max_length = 0 
        for index, letter in enumerate(s):
            if letter in letters:
                distance = max(letters[letter], distance) 
            max_length = max(max_length, index - distance + 1)
            letters[letter] = index + 1
        return max_length



        
print(Solution().lengthOfLongestSubstring('dvdf'))
#print(Solution().lengthOfLongestSubstring('pwwkew'))