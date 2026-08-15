class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for letter1 in s:
            s_dict[letter1] += 1

        for letter2 in t:
            t_dict[letter2] += 1
        
        for letter,freq in s_dict.items():
            if t_dict[letter] != freq:
                return False
        return True
