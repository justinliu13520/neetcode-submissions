class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_l, outer_r = 0, len(matrix)-1
        while outer_l <= outer_r:
            outer_m = outer_l + ((outer_r-outer_l) // 2)
            inner_l = 0
            inner_r = len(matrix[outer_m])-1
            print("checking:",matrix[outer_m], inner_l,inner_r)
            if target >= matrix[outer_m][inner_l] and target <=  matrix[outer_m][inner_r]:
                print("Potentially found")
                return self.search(matrix[outer_m],target)
            elif target < matrix[outer_m][inner_l]:
                outer_r = outer_m - 1
                print("old l",outer_l,"new r",outer_r)
            elif target > matrix[outer_m][inner_r]:
                outer_l = outer_m + 1
                print("new l",outer_l,"old r",outer_r)
        return False

    