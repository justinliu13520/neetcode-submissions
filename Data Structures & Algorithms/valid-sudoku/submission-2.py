class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We have to keep track of each row, column, and square for duplicates
        rows = defaultdict(set) # We use set to make sure we don't have duplicates
        cols = defaultdict(set)
        squares = defaultdict(set)

        # We have to loop through the whole board no matter what

        for row in range(9):
            for col in range(9):
                # We don't care about . since they dont tell us if there are dupes
                if board[row][col] == ".":
                    continue
                current_tile = board[row][col]
                if (current_tile in rows[row] or # Check the current row for dupes
                    current_tile in cols[col] or # Check the current col for dupes
                     current_tile in squares[(row // 3, col // 3)]): #check the current square for dupes
                     return False

                # no dupes found so add to current row, col, square for future dupe checks
                rows[row].add(current_tile)
                cols[col].add(current_tile)
                squares[(row // 3,col // 3)].add(current_tile)
        return True
                
                