class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        for l in t:
            t_dict[l] += 1
        
        l = 0
        res,min_len = [-1,-1], float("inf")
        have,need = 0, len(t_dict)

        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s[r] in t and t_dict[s[r]] == s_dict[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l,r]
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if min_len != float("inf") else ""

                
                








