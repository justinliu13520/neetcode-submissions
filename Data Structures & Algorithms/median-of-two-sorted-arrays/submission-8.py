class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter,longer = nums1,nums2

        if len(nums1) > len(nums2):
            shorter,longer = nums2,nums1
        
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2
        l,r = 0, len(shorter) - 1
        while True:
            i = (l + r) // 2
            j = half_len - i - 2

            shorter_right = shorter[i] if i >= 0 else float("-inf")
            shorter_left = shorter[i + 1] if i + 1 < len(shorter) else float("inf")
            longer_right = longer[j] if j >= 0 else float("-inf")
            longer_left = longer[j + 1] if j + 1 < len(longer) else float("inf")

            if shorter_left >= longer_right and longer_left >= shorter_right:
                if total_len % 2:
                    return min(shorter_left,longer_left)
                else:
                    return (min(shorter_left,longer_left) + max(shorter_right,longer_right)) / 2
            elif shorter_left < longer_right:
                l = i + 1
            else:
                r = i - 1