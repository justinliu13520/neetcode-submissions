class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        for letter in s:
            if s_dict[letter] != t_dict[letter]:
                return False
        return True

