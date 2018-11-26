class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        current = 0
        step = 1
        
        new_string = [''] * numRows
        for c in s:
            new_string[current] += c
            if current == 0:
                step = 1
            elif current == numRows - 1:
                step = -1
            current += step
        
        return ''.join(new_string)
