这道题要求我们划分链表，把所有小于给定值的节点都移到前面，大于该值的节点顺序不变，相当于一个局部排序的问题。

设定两个虚拟节点，dummyHead1用来保存小于于该值的链表，dummyHead2来保存大于等于该值的链表
遍历整个原始链表，将小于该值的放于dummyHead1中，其余的放置在dummyHead2中
遍历结束后，将dummyHead2插入到dummyHead1后面


class Solution:
  def partition(self, head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next
