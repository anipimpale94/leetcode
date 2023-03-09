# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 4. Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A

        t = len(A) + len(B)
        l, r, h = 0, len(A) - 1, t // 2

        while True:
            i = (l + r) // 2
            j = h - 1 - i - 1

            AL = A[i] if i >= 0 else float('-infinity')
            AR = A[i+1] if i+1 < len(A) else float('infinity')
            BL = B[j] if j >= 0 else float('-infinity')
            BR = B[j+1] if j+1 < len(B) else float('infinity')

            if AL <= BR and BL <= AR:
                if t % 2:
                    return min(AR, BR)
                else:
                    return (min(AR, BR) + max(AL, BL)) / 2
            elif AL > BR:
                r = i - 1
            else:
                l = i + 1

print('nums1 = [1,3], nums2 = [2]')
print(Solution().findMedianSortedArrays([1,3], [2]))
print('-----------------')
print('nums1 = [1,2], nums2 = [3,4]')
print(Solution().findMedianSortedArrays([1,2], [3,4]))
print('-----------------')
print('nums1 = [1,2,3,4], nums2 = [5,6,7]')
print(Solution().findMedianSortedArrays([1,2,3,4], [5,6,7]))
print('-----------------')
print('nums1 = [0,0], nums2 = [0,0]')
print(Solution().findMedianSortedArrays([0,0], [0,0]))
print('-----------------')
print('nums1 = [], nums2 = [1]')
print(Solution().findMedianSortedArrays([], [1]))