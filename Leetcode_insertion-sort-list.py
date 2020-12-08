
#https://leetcode.com/problems/insertion-sort-list/submissions/
#Author: Ossie Ackermann
#Date: 2020/Dec/07

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode):
        output = ListNode()
        while head:
            prev = output
            #locating head.val
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            #prev = (a,b),    a< head.val < b
            prev.next = ListNode(head.val,prev.next)
            head = head.next
        return output.next
            
            