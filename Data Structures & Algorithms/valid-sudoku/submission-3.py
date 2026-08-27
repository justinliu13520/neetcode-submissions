class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        square_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                tile = board[row][col]
                if tile == ".":
                    continue
                if (tile in row_dict[row] or
                    tile in col_dict[col] or
                     tile in square_dict[(row//3,col//3)]):
                     return False
                
                row_dict[row].add(tile)
                col_dict[col].add(tile)
                square_dict[(row//3,col//3)].add(tile)
        return True
