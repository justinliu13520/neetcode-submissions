class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if (value in cols[col]
                    or value in rows[row]
                    or value in squares[(row // 3, col // 3)]):
                    return False
                cols[col].add(value)
                rows[row].add(value)
                squares[(row // 3,col // 3)].add(value)
        return True