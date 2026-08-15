class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for letter in t:
            t_dict[letter] += 1

        have, need = 0, len(t_dict)
        min_length = float("inf")
        res = [-1,-1]
        l = 0

        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s[r] in t and t_dict[s[r]] == s_dict[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < min_length:
                    min_length = r-l+1
                    res = [l,r]
                s_dict[s[l]] -= 1
                if s[l] in t and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if min_length != float("inf") else ""
                








