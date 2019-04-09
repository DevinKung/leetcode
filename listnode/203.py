# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = None
        prev = None
        
        while head != None:
            
            if head.val == val:
                if prev != None:
                    prev.next = head.next
                    head = head.next
                    continue
                
                head = head.next
                continue
            
            if not prev:
                start = head
                
            prev = head
            
            head = head.next
        
        return start
            
                
                