class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter_array, longer_array = nums1, nums2
        if len(nums2) <= len(nums1):
            shorter_array, longer_array = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l,r = 0, len(shorter_array) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            shorter_left = shorter_array[i] if i >= 0 else float("-inf")
            shorter_right = shorter_array[i+1] if i + 1< len(shorter_array) else float("inf")
            longer_left = longer_array[j] if j >= 0 else float("-inf")
            longer_right = longer_array[j+1] if j + 1 < len(longer_array) else float("inf")

            if shorter_left <= longer_right and longer_left <= shorter_right:
                if total % 2 == 1:
                    return min(longer_right,shorter_right)
                else:
                    return (max(shorter_left,longer_left) + min(shorter_right,longer_right)) / 2
            elif shorter_left > longer_right:
                r = i - 1
            else:
                l = i + 1