class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row, bottom_row = 0, len(matrix) - 1
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
            if matrix[mid_row][0] > target:
                bottom_row = mid_row - 1
            elif matrix[mid_row][-1] < target:
                top_row = mid_row + 1
            else:
                break
        if top_row > bottom_row:
            return False
        cur_row = (top_row + bottom_row) // 2

        l,r = 0, len(matrix[cur_row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[cur_row][m] > target:
                r = m - 1
            elif matrix[cur_row][m] < target:
                l = m + 1
            else:
                return True
        return False