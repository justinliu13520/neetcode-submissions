class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l < r:
            sum_total = numbers[l] + numbers[r]
            if sum_total == target:
                return [l+1,r+1]
            elif sum_total < target:
                l += 1
            else:
                r -= 1
        return []