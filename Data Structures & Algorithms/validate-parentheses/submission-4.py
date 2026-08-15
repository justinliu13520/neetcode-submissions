class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = deque()
        for thing in s:
            if thing == "(" or thing == "[" or thing == "{":
                stack.append(thing)
            else:
                if not stack:
                    return False
                matching = stack.pop()
                if ((thing == ")" and matching != "(")) or ((thing == "}" and matching != "{")) or ((thing == "]" and matching != "[")):
                    return False
        if len(stack) != 0:
            return False 
        return True
