class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1

        matches = 0
        for l in s1_dict:
            matches += 1 if s1_dict.get(l) == s2_dict.get(l) else 0
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == len(s1_dict):
                return True
            cur_letter = s2[r]
            s2_dict[cur_letter] += 1
            if cur_letter in s1_dict:
                if s2_dict[cur_letter] == s1_dict[cur_letter]:
                    matches += 1
                elif s2_dict[cur_letter] == s1_dict[cur_letter] + 1:
                    matches -= 1
            
            left_letter = s2[l]
            s2_dict[left_letter] -= 1
            if left_letter in s1_dict:
                if s2_dict[left_letter] == s1_dict[left_letter]:
                    matches += 1
                elif s2_dict[left_letter] == s1_dict[left_letter] - 1:
                    matches -= 1
            l += 1
        return matches == len(s1_dict)








