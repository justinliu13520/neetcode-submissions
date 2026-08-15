class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_list = ["+","-","*","/"]
        stack = []

        for t in tokens:
            if t not in operation_list:
                stack.append(int(t))
            else:
                rightVal = stack.pop()
                leftVal = stack.pop()
                if t == "+":
                    stack.append(leftVal+rightVal)
                elif t == "*":
                    stack.append(leftVal*rightVal)
                elif t == "-":
                    stack.append(leftVal-rightVal)
                elif t == "/":
                    stack.append(int(leftVal/rightVal))
        return int(stack[0])