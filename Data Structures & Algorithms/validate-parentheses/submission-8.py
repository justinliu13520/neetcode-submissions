class Solution:
    def isValid(self, s: str) -> bool:
        #if odd, then dont even check because wont be valid
        if len(s) % 2 != 0:
            return False
        stack = []
        rightParentheses = "{[("
        for c in s:
            if c in rightParentheses:
                stack.append(c)
            else:
                # if empty and we have a thing to check, then that means no matches
                if len(stack) == 0:
                    return False
                if c == ")" and stack.pop() != "(":
                    return False
                if c == "}" and stack.pop() != "{":
                    return False
                if c == "]" and stack.pop() != "[":
                    return False
        return len(stack) == 0