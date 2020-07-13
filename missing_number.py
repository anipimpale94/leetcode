# You are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Example
# Input: a = [0,1,2,4,5,6]
# Input: n = 5
# Output: 3

class Solution:
  """ 
  Class having solution for the problem 
  """

  def get_missing_number(self, a, n):
    """
    Calculate the missing number of an array

    :param list a: List from which missing number has to be found
    :param int n: Total number of elements in array
    :return: missing number
    :rtype: int
    """
    sum = (n+1)*(n+2)/2
    for element in a:
      sum = sum - element

    return sum

print(Solution().get_missing_number([0,1,2,4,5,6], 5))