class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for s_letter in s:
            dict1[s_letter] += 1
        for t_letter in t:
            dict2[t_letter] += 1
        
        for letter in dict1.keys():
            if dict1[letter] != dict2[letter]:
                return False
        return True