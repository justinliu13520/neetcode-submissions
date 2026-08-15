class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        matches = 0

        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        for key in s1_dict.keys():
            matches += 1 if s1_dict[key] == s2_dict.get(key, 0) else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1_dict):
                return True

            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1
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
            l += 1  # unindented — always runs

        return matches == len(s1_dict)