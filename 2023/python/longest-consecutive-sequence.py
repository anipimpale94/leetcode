# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence

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