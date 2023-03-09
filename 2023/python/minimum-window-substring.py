# https://leetcode.com/problems/minimum-window-substring/
# 76. Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        currentMap, resultMap = {}, {}
        currentCount = 0
        for c in t:
            currentMap[c], resultMap[c] = 0, 1 + resultMap.get(c, 0)

        resultCount = len(resultMap)
        l, r = 0, -1
        res, resLen = [-1, -1], len(s)
        for i in s:
            r += 1
            if i not in resultMap:
                continue
            
            currentMap[i] = 1 + currentMap[i]
            if currentMap[i] == resultMap[i]:
                currentCount += 1
            
            if resultCount == currentCount:
                currentLen = len(s[l:r+1])
                if resLen >= currentLen:
                    res = [l, r]
                    resLen = currentLen
                
                while l < len(s):
                    if s[l] in resultMap:
                        currentMap[s[l]] = currentMap[s[l]] - 1

                        if currentMap[s[l]] < resultMap[s[l]]:
                            currentCount -= 1

                    l += 1
                    if resultCount != currentCount:
                        break

                    currentLen = len(s[l:r+1])
                    if resLen >= currentLen:
                        res = [l, r]
                        resLen = currentLen

        return resLen == len(s) if "" else s[res[0]:res[1]+1]

print('s = "", t=""')
print('"' + Solution().minWindow('', '') + '"')
print('-----------------')
print('s = "a", t= "a"')
print('"' + Solution().minWindow('a', 'a') + '"')
print('-----------------')
print('s = "a", t= "aa"')
print('"' + Solution().minWindow('a', 'aa') + '"')
print('-----------------')
print('s = "ADOBECODEBANC", t= "ABC"')
print('"' + Solution().minWindow("ADOBECODEBANC", "ABC") + '"')
print('-----------------')
print('s = "ADOBECODEBANC", t= "ZZZ"')
print('"' + Solution().minWindow("ADOBECODEBANC", "ZZZ") + '"')
print('-----------------')
print('s = "aaaaaaaaaaaabbbbbcdd", t= "abcdd"')
print('"' + Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") + '"')
    