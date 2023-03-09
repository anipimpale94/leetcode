# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# Example:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequenceCount = 0
        tempNums = set(nums)
        for num in tempNums:
            if (num - 1) in tempNums:
                continue

            count = 1
            while (num + count) in tempNums:
                count += 1

            longestSequenceCount = max(count, longestSequenceCount)

        return longestSequenceCount

print('nums = []')
print('Result:', Solution().longestConsecutive([])) 
print('-----------------')
print('nums = [100,4,200,1,3,2]')
print('Result:', Solution().longestConsecutive([100,4,200,1,3,2]))
print('-----------------')
print('nums = [0,3,7,2,5,8,4,6,0,1]')
print('Result:', Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))