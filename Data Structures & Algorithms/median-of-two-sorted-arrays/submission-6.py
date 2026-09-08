class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter, longer = nums1, nums2
        if len(nums2) <= len(nums1):
            shorter,longer = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l,r = 0, len(shorter) - 1
        while True:
            i = (r + l) // 2
            j = half - i - 2

            shorter_left = shorter[i] if i >= 0 else float("-inf")
            shorter_right = shorter[i+1] if i + 1 < len(shorter) else float("inf")
            longer_left = longer[j] if j >= 0 else float("-inf")
            longer_right = longer[j+1] if j + 1 < len(longer) else float("inf")

            if shorter_left <= longer_right and longer_left <= shorter_right:
                if total % 2:
                    return min(longer_right,shorter_right)
                else:
                    return (max(longer_left,shorter_left) + min(longer_right,shorter_right)) / 2
            elif shorter_left > longer_right:
                r = i - 1
            else:
                l = i + 1
