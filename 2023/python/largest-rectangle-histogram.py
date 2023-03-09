# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram

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
