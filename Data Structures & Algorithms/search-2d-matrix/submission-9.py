class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix)-1

        while top_row<=bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
            elif matrix[middle_row][-1] < target:
                top_row = middle_row + 1
            else:
                break
            
        if not (bottom_row >= top_row):
            return False
        cur_row = (top_row + bottom_row) // 2

        l,r = 0, len(matrix[cur_row]) -1

        while l<=r:
            m=(l+r)//2
            n=matrix[cur_row][m]
            if n>target:
                r=m-1
            elif n < target:
                l=m+1
            else:
                return True
        return False


             







