class Solution:
    def isValid(self, s: str) -> bool:
        leftParenth = ['[','(','{']
        stack = []
        for thing in s:
            if thing in leftParenth:
                stack.append(thing)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if thing == ']':
                    if popped != '[':
                        return False
                elif thing == '}':
                    if popped != '{':
                        return False
                elif thing == ')':
                    if popped != '(':
                        return False

        print(len(stack))
        return len(stack) == 0