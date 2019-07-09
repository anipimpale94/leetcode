# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(nums)
        
        