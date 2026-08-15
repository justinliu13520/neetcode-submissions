class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        left_paren = ['(','[','{']
        stack = []
        for paren in s:
            if paren in left_paren:
                stack.append(paren)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if paren == ')' and popped != '(':
                    return False
                if paren == '}' and popped != '{':
                    return False
                if paren == ']' and popped != '[':
                    return False
        return len(stack) == 0