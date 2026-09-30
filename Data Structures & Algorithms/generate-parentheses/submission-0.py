class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []

        left = ["("]
        for thing in s:
            if thing in left:
                stack.append(thing)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if thing == ")" and not popped == "(":
                    return False
        return True if len(stack) == 0 else False
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_string):
            print(cur_string)
            if len(cur_string) == 2*n:
                if self.isValid(cur_string):
                    res.append(cur_string)
                return
                
            dfs(cur_string+"(")
            dfs(cur_string+")")
        dfs("")
        return res





