class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        integer_string = [0]
        negation = 1 

        if x < 0:
            negation = -1
            x *= negation
        while x != 0:
            remainder = x % 10
            x = int(x / 10)
            integer_string.append(remainder)        
        result = negation * int(''.join(map(str, integer_string)))
        if result > 2**31 - 1 or result < -2**31:
            return 0
        else:
            return result