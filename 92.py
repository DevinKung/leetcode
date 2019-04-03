

class Solution():
  def reverseBetween(self, head, m, n):
    dummy = pre = ListNode(0)
    dummy.next = head
    for _ in xrange(m-1):
        pre = pre.next
    cur= pre.next
    # reverse the defined part 
    node = None
    for _ in xrange(n-m+1):
        nxt = cur.next
        cur.next = node
        node = cur
        cur= nxt
    # connect three parts
    pre.next.next = cur
    pre.next = node
    return dummy.next
