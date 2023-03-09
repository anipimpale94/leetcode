# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.
#
# Example
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
# Input: heights = [2,4]
# Output: 4

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        stack = []      
        result, currentMax = 0, 0
        for idx, h in enumerate(heights):
            if h >= currentMax:
                stack.append((idx, h))
                currentMax = h
            else:
                lastIndex = idx
                while True:
                    if stack and stack[-1][1] > h:
                        lastIndex, value = stack.pop()
                        result = max(result, value * (idx - lastIndex))
                    else: 
                        break
                stack.append((lastIndex, h))

        while stack:
            lastIndex, value = stack.pop()
            result = max(result, value * (len(heights) - lastIndex))

        return result
    
print('height = []')
print(Solution().largestRectangleArea([]))
print('-----------------')
print('height = [2,1,5,6,2,3]')
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print('-----------------')
print('height = [2,4]')
print(Solution().largestRectangleArea([2,4]))
