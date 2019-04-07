
 def postorderTraversal(self, root):
        if not root: return []
        result, stack = [], [root]
        
        while stack:
            # pop the element from stack and push it into result stack
            root = stack.pop()
            result.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result[::-1]
