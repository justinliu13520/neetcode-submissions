class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_t = defaultdict(int)
        dict_s = defaultdict(int)

        for letter in s:
            dict_s[letter] += 1
        
        for letter in t:
            dict_t[letter] += 1

        for key in dict_s.keys():
            if dict_t[key] != dict_s[key]:
                return False
        
        return True