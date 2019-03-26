# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # n is the node of l1
        n = l1
        i = 1
        num_l1 = 0
        # get num of l1
        while n:
            num_l1 = num_l1 + n.val * i
            i = i * 10
            n = n.next

        # m is the node of l2
        m = l2
        j = 1
        num_l2 = 0
        # get num of l2
        while m:
            num_l2 = num_l2 + m.val * j
            j = j * 10
            m = m.next
        # get the sum of l1 , l2
        str_num = str(num_l1 + num_l2)
        # reverse str_num
        str_num = str_num[::-1]
        # turn to list output
        list_result = []
        for s in str_num:
            list_result.append(int(s))
        return list_result
