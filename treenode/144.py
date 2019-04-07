用栈(Stack)的思路来处理问题。

前序遍历的顺序为根-左-右，具体算法为：

把根节点push到栈中
循环检测栈是否为空，若不空，则取出栈顶元素，保存其值
看其右子节点是否存在，若存在则push到栈中
看其左子节点，若存在，则push到栈中。

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        re,stack=[],[root]
        while len(stack)>0:
            item=stack.pop()
            if item!=None:
                re.append(item.val)
                stack.append(item.right)
                stack.append(item.left)
            else:
                continue
        return re
        
       
 another solution:
         if root is None:return []
        def proNode(root:TreeNode,l:list):
                l.append(root.val)
                if root.left: proNode(root.left,l)
                if root.right:proNode(root.right,l)
        l = []
        proNode(root,l)  return l
