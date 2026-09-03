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

        for letter in s1_dict:
            matches += 1 if s1_dict.get(letter,-1) == s2_dict.get(letter,-1) else 0

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == len(s1_dict):
                return True
            s2_dict[s2[r]] += 1
            if s2[r] in s1_dict:
                if s2_dict[s2[r]] == s1_dict[s2[r]]:
                    matches += 1
                elif s2_dict[s2[r]] == s1_dict[s2[r]] + 1:
                    matches -= 1

            s2_dict[s2[l]] -= 1
            if s2[l] in s1_dict:
                if s2_dict[s2[l]] == s1_dict[s2[l]]:
                    matches += 1
                elif s2_dict[s2[l]] == s1_dict[s2[l]] - 1:
                    matches -= 1
            l += 1
        return len(s1_dict) == matches