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
        for letter in s1:
            matches += 1 if s1_dict.get(letter) == s2_dict.get(letter) else 0
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == len(s1_dict):
                return True

            cur_char = s2[r]
            s2_dict[cur_char] += 1
            if cur_char in s1:
                if s2_dict[cur_char] == s1_dict[cur_char]:
                    matches += 1
                elif s2_dict[cur_char] == s1_dict[cur_char] + 1:
                    matches -= 1
             
            left_char = s2[l]
            s2_dict[left_char] -= 1
            if left_char in s1:
                if s2_dict[left_char] == s1_dict[left_char]:
                    matches += 1
                elif s2_dict[left_char] == s1_dict[left_char] - 1:
                    matches -= 1
            l += 1
        return matches == len(s1_dict)










