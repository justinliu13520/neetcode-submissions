class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set) # row val
        COLS = defaultdict(set) # col val
        SQR = defaultdict(set) #tuple val

        for row in range(9):
            for col in range(9):
                cell_val = board[row][col]
                if cell_val == ".":
                    continue
                if (cell_val in ROWS[row] or 
                    cell_val in COLS[col] or
                    cell_val in SQR[(row//3,col//3)]):
                    return False
                ROWS[row].add(cell_val)
                COLS[col].add(cell_val)
                SQR[(row//3,col//3)].add(cell_val)
        return True


