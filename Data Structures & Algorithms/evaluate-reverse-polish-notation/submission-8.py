class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","*","-","/"]
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                right_val = int(stack.pop())
                left_val = int(stack.pop())
                if token == "+":
                    stack.append(left_val+right_val)
                elif token == "-":
                    stack.append(left_val-right_val)
                elif token == "*":
                    stack.append(left_val*right_val)
                else:
                    stack.append(int(left_val/right_val))
        return int(stack[0])