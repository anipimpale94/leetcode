# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:

# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while(temp is not None and temp.next is not None): 
            temp.val, temp.next.val = temp.next.val, temp.val  
            temp = temp.next.next    
        return head