class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bottom_row = 0, ROWS-1

        # Binary search the rows to find which row the target is on
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if matrix[middle_row][0] > target: 
                # Because the first number of each row is bigger than the last row, 
                # we use this to get rid of everything after this row
                bottom_row = middle_row - 1
            elif matrix[middle_row][-1] < target:
                # If first number of the row is not bigger, this means the target is on the current row
                # or on the rows after. We use the last number of the current row to check if on this row.
                # If smaller than our target, we know it's not on this row
                top_row = middle_row + 1
            else:
                # We break now that we found our row
                break
        
        if not top_row <= bottom_row:
            return False
        l, r = 0, COLS-1
        row = (top_row + bottom_row) //2
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m -1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
