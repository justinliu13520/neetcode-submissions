class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        left = ["(","{","["]
        stack = []
        for thing in s:
            if thing in left:
                stack.append(thing)
            else:
                if not stack:
                    return False
                if thing == ")" and stack.pop() != "(":
                    return False
                elif thing == "}" and stack.pop() != "{":
                    return False
                elif thing == "]" and stack.pop() != "[":
                    return False
        return len(stack) == 0