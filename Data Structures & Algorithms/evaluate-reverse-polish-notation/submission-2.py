class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isNum(val):
            if val == "+" or val == "-" or val == "*" or val == "/":
                return False
            return True
        stack = deque()
        for t in tokens:
            if isNum(t):
                stack.append(int(t))
            else:
                rightVal = stack.pop()
                leftVal = stack.pop()
                if t == "+":
                    stack.append(rightVal+leftVal)
                if t == "-":
                    stack.append(leftVal-rightVal)
                if t == "*":
                    stack.append(leftVal*rightVal)
                if t == "/":
                    stack.append(int(leftVal/rightVal))
        return stack[0]