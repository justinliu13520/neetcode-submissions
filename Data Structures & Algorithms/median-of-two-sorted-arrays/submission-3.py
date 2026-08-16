class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter_array,longer_array = nums1,nums2
        if len(nums2) < len(nums1):
            shorter_array,longer_array = nums2,nums1
        
        total_len = len(nums1) + len(nums2)
        half = total_len // 2

        l,r = 0,len(shorter_array) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            s_left = shorter_array[i] if i >= 0 else float("-inf")
            s_right = shorter_array[i+1] if i+1 < len(shorter_array) else float("inf")
            l_left = longer_array[j] if j >= 0 else float("-inf")
            l_right = longer_array[j+1] if j+1 < len(longer_array) else float("inf")

            if s_left <= l_right and l_left <= s_right:
                if total_len % 2 == 1:
                    return min(l_right,s_right)
                else:
                    return (max(s_left,l_left) + min(l_right,s_right)) / 2
            elif s_left > l_right:
                r = i - 1
            else:
                l = i + 1
