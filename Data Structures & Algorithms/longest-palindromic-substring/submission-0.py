class Solution:
    def longestPalindrome(self, s: str) -> str:        
        result_index = 0
        result_len = 0
        for i in range(len(s)):
            l,r = i,i
            #odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result_index = l
                    result_len = r - l + 1
                l -= 1
                r += 1

            #even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result_index = l
                    result_len = r - l + 1
                l -= 1
                r += 1

        return s[result_index:result_index+result_len]