class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_list = ["+","-","*","/"]
        stack = []

        for t in tokens:
            if t not in operation_list:
                stack.append(int(t))
            else:
                if t == "+":
                    right_val = stack.pop()
                    left_val = stack.pop()
                    stack.append(left_val+right_val)
                elif t == "-":
                    right_val = stack.pop()
                    left_val = stack.pop()
                    stack.append(left_val-right_val)
                elif t == "*":
                    right_val = stack.pop()
                    left_val = stack.pop()
                    stack.append(left_val*right_val)
                elif t == "/":
                    right_val = stack.pop()
                    left_val = stack.pop()
                    stack.append(int(left_val/right_val))
        return stack[0]