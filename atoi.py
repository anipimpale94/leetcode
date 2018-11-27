import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        number_string = "".join(re.findall("^[-+]?[0-9]*\d", str.strip()))
        if number_string == "" or number_string == "+":
            return 0
        if "-" in number_string and number_string.find("-") != 0:
                return number_string          
        number = int(number_string)
        if number > (1<<31) - 1:
            number = (1<<31) - 1
        if number < -1*(1<<31):
            number = -1*(1<<31)
        return number