class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        visited = set()

        LEFT, TOP = 0,0
        RIGHT, BOTTOM = len(board[0])-1,len(board)-1
        
        def dfs(row,col,j):
            if j == len(word):
                return True
            if (row < 0 or row > BOTTOM or col < 0 or col > RIGHT
                    or (row, col) in visited
                    or board[row][col] != word[j]):
                return False
            
            visited.add((row,col))
            found = (dfs(row+1, col, j+1) or dfs(row-1, col, j+1) or
                     dfs(row, col+1, j+1) or dfs(row, col-1, j+1))
            visited.remove((row,col))
            return found
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
