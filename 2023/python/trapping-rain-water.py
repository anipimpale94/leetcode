# Link https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        result = 0
        tempResult = []
        currentMax = height[0]
        for h in height:
            if h < currentMax:
                tempResult.append(currentMax - h)
                continue

            result += sum(tempResult)
            tempResult = []
            currentMax = h

        if tempResult:
            pointer = currentMax          
            for r in reversed(tempResult):
                if r > pointer:
                    result += r - pointer
                else:
                    pointer = r
                
        return result

print('height = []')
print(Solution().trap([]))
print('-----------------')
print('height = [0,1,0,2,1,0,1,3,2,1,2,1]')
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('-----------------')
print('height = [4,2,0,3,2,5]')
print(Solution().trap([4,2,0,3,2,5]))
print('-----------------')
print('height = [0,7,1,4,6]')
print(Solution().trap([0,7,1,4,6]))


