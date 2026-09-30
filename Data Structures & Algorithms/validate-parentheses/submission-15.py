class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []

        left = ["(","[","{"]
        for thing in s:
            if thing in left:
                stack.append(thing)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if thing == ")" and not popped == "(":
                    return False
                elif thing == "]" and not popped == "[":
                    return False
                elif thing == "}" and not popped == "{":
                    return False
        return True if len(stack) == 0 else False