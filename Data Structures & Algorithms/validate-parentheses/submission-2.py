class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        rightParentheses = "{[("
        for c in s:
            if c in rightParentheses:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ")" and stack.pop() != "(":
                    return False
                if c == "}" and stack.pop() != "{":
                    return False
                if c == "]" and stack.pop() != "[":
                    return False
        if len(stack) > 0:
            return False
        return True