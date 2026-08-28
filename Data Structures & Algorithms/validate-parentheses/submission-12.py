class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        right_paren = [")","]","}"]

        stack = []
        for paren in s:
            if paren not in right_paren:
                stack.append(paren)
            else:
                if not stack:
                    return False
                cur_left = stack.pop()
                if paren == ")" and cur_left != "(":
                    return False
                if paren == "}" and cur_left != "{":
                    return False
                if paren == "]" and cur_left != "[":
                    return False
        return len(stack) == 0