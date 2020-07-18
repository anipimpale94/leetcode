# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
# Return true if the sum exists and return false if it does not.

# Example
# Input: elements: [5, 7, 1, 2, 8, 4, 3]
# Input: value: 12
# Output: True

# Input: elements: [5, 7, 1, 2, 8, 4, 3]
# Input: value: 14
# Output: False

class Solution:
  """
  Class having solution for the problem 
  """

  def check_sum_of_integers_is_equal(self, elements, sum_value):
    """
    Determine whether sum of two interger is equal to value

    :param list elements: List from which missing number has to be found
    :param int sum_value: Total number of elements in array
    :rtype: bool
    """
    sum_values = set()
    for element in elements:
      if sum_value - element in sum_values:
        return True
      sum_values.add(element)
    return False

elements = [5, 7, 1, 2, 8, 4, 3]
sum_value = 14
print(Solution().check_sum_of_integers_is_equal(elements, sum_value))


