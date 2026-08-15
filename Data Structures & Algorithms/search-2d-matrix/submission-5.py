class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row,r_row = 0, len(matrix) - 1
        while l_row <= r_row:
            mid_row = (r_row + l_row) // 2
            if matrix[mid_row][0] > target:
                r_row = mid_row - 1
            elif matrix[mid_row][-1] < target:
                l_row = mid_row + 1
            else:
                break
        if not l_row <= r_row:
            return False
        target_row = (l_row + r_row) // 2
        l,r = 0, len(matrix[target_row]) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[target_row][m] > target:
                r = m - 1
            elif matrix[target_row][m] < target:
                l = m + 1
            else:
                return True
        return False