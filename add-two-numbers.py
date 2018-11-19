# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        carry = 0
        head = output = ListNode(None)
        while l1 != None or l2 != None:          
            sum = 0 + carry
            if l1 != None:                
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            output.next = ListNode(sum%10)
            carry = 0
            if sum > 9:
                carry = 1      
            output = output.next
        if carry == 1:
            output.next = ListNode(1)
        return head.next