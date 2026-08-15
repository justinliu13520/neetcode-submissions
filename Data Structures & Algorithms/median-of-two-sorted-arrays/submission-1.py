class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2 # A will be the shorter of the two arrays
        if len(nums2) < len(nums1):
            A,B = B,A
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = l + (r - l) // 2
            j = half - i - 2 # minus 2 because we need to account for both the 0 index of A and B, so minus 1 each
            
            # we say negative infinity because if i is ever negative, we are out of bound to the left. We use negative infinity
            # because we only use left for max when finding the median when total is even
            # We say infinity for when i + 1 out of bound because i + 1 out of bound means on the right, so we want a big value for when we use min
            Aleft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= ARight:
                if total % 2 == 1: #meaning total len is odd so only 1 median
                    return min(ARight,Bright)
                else:
                    return (max(Aleft,Bleft) + min(ARight,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1