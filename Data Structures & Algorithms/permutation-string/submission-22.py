class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1
        
        match = 0
        for letter in s1_dict:
            match += 1 if s1_dict.get(letter,0) == s2_dict.get(letter,0) else 0
        
        l = 0
        for r in range(len(s1),len(s2)):
            if match == len(s1_dict):
                return True
            cur_letter = s2[r]
            s2_dict[cur_letter] += 1
            if cur_letter in s1_dict:
                if s1_dict[cur_letter] == s2_dict[cur_letter]:
                    match += 1
                elif s1_dict[cur_letter] + 1 == s2_dict[cur_letter]:
                    match -= 1
            dropped_letter = s2[l]
            s2_dict[dropped_letter] -= 1
            if dropped_letter in s1_dict:
                if s1_dict[dropped_letter] == s2_dict[dropped_letter]:
                    match += 1
                elif s1_dict[dropped_letter] - 1 == s2_dict[dropped_letter]:
                    match -= 1
            l += 1
        return match == len(s1_dict)






