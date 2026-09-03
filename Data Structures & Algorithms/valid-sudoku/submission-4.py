class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sqr_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur_tile = board[row][col]
                if cur_tile == ".":
                    continue
                if (cur_tile in row_dict[row] or
                    cur_tile in col_dict[col] or
                     cur_tile in sqr_dict[(row//3,col//3)]):
                     return False
                row_dict[row].add(cur_tile)
                col_dict[col].add(cur_tile)
                sqr_dict[(row//3,col//3)].add(cur_tile)
        return True