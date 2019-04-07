用栈(Stack)的思路来处理问题。

后序遍历的顺序为左-右-根，具体算法为：

先将根结点压入栈，然后定义一个辅助结点head
while循环的条件是栈不为空
在循环中，首先将栈顶结点t取出来
如果栈顶结点没有左右子结点，或者其左子结点是head，或者其右子结点是head的情况下。我们将栈顶结点值加入结果res中，并将栈顶元素移出栈，然后将head指向栈顶元素
否则的话就看如果右子结点不为空，将其加入栈
再看左子结点不为空的话，就加入栈

another solution:
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
