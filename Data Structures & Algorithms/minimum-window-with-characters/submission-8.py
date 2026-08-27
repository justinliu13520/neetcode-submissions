class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        for letter in t:
            t_dict[letter] += 1
        have,need = 0,len(t_dict)
        min_len,res = len(s) + 1,[-1,-1]
        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s[r] in t_dict and t_dict[s[r]] == s_dict[s[r]]:
                have += 1

            while have == need:
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    res = [l,r]
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1         
        l,r = res
        return s[l:r+1] if min_len != len(s) + 1 else ""

                   
                