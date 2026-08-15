class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_list = ["+","-","*","/"]
        res = deque()

        for t in tokens:
            if t not in operation_list:
                res.append(int(t))            
            else:
                secondNum = res.pop()
                firstNum = res.pop()
                if t == "+":
                    res.append(int(firstNum+secondNum))
                elif t == "-":
                    res.append(int(firstNum-secondNum))  
                elif t == "*":
                    res.append(int(firstNum*secondNum)) 
                elif t == "/":
                    res.append(int(firstNum/secondNum))
                print(res)
        return res.popleft()                 
