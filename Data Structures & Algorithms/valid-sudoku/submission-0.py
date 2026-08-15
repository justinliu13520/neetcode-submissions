class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            valid_dict = set()
            for col in range(9):   
                if board[row][col] == ".":
                    continue
                if board[row][col] not in valid_dict:
                    valid_dict.add(board[row][col])
                else:
                    return False
        for col in range(9):
            valid_dict = set()
            for row in range(9): 
                if board[row][col] == ".":
                    continue  
                if board[row][col] not in valid_dict:
                    valid_dict.add(board[row][col])
                else:
                    return False
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True