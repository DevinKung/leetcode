思路：

这里我们使用栈。

遍历输入字符串
如果当前字符为左半边括号时，则将其压入栈中
如果遇到右半边括号时，分类讨论：
1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环  
2）若此时栈为空，则直接返回false
3）若不为对应的左半边括号，反之返回false


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
