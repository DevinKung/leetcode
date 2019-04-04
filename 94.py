中序遍历的顺序为左-根-右

class Solution:
    def inorderTraversal(self, root):
        stack = [ (False, root) ]
        acc = []
        
        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append( (False, val.right) )
                    stack.append( (True, val) )
                    stack.append( (False, val.left) )
                else:
                    acc.append( val.val )
        return acc
