中序遍历的顺序为左-根-右
栈的思想
Simple, understandable solution. In the loop: If we get a node with flag false, we add children in correct order and set them to false. because they have to be processed (for their children). And we set flag of current node to true.

If we get node with flag set to true we simply print its value (add to acc).
Can be modified to do post and pre order too.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
