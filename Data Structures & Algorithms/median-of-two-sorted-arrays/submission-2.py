class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter_array, longer_array = nums1,nums2
        if len(nums2) < len(nums1):
            shorter_array,longer_array = nums2,nums1
        
        total_len = len(nums1) + len(nums2)
        half = total_len // 2

        l,r = 0,len(shorter_array) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            shorter_array_left = shorter_array[i] if i >= 0 else float("-inf")
            shorter_array_right = shorter_array[i + 1] if i + 1 < len(shorter_array) else float("inf")
            longer_array_left = longer_array[j] if j >= 0 else float("-inf")
            longer_array_right = longer_array[j + 1] if j + 1 < len(longer_array) else float("inf")

            if shorter_array_left <= longer_array_right and longer_array_left <= shorter_array_right:
                if total_len % 2 == 1:
                    return min(longer_array_right,shorter_array_right)
                else:
                    return (max(longer_array_left,shorter_array_left) + min(longer_array_right,shorter_array_right)) / 2
            elif shorter_array_left > longer_array_right:
                r = i - 1
            else:
                l = i + 1