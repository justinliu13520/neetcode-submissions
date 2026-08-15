class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # a sliding window that is always length of s1
        # conditions for matches increasing
        # letter being changed is in s1 and matches the frequency of s1 after change
        # condition for matches decreasing
        # change resulted in a difference of one from s1

        if len(s1) > len(s2):
            return False

        small_str_dict = defaultdict(int)
        big_str_dict = defaultdict(int)
        for i in range(len(s1)):
            small_str_dict[s1[i]] += 1
            big_str_dict[s2[i]] += 1
        
        matches = 0
        for letter in small_str_dict.keys():
            matches += 1 if small_str_dict[letter] == big_str_dict[letter] else 0

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == len(small_str_dict):
                return True
            big_str_dict[s2[r]] += 1
            if s2[r] in small_str_dict:
                if big_str_dict[s2[r]] == small_str_dict[s2[r]]:
                    matches += 1
                elif big_str_dict[s2[r]] == small_str_dict[s2[r]] + 1:
                    matches -= 1
            
            big_str_dict[s2[l]] -= 1
            if s2[l] in small_str_dict:
                if big_str_dict[s2[l]] == small_str_dict[s2[l]]:
                    matches += 1
                elif big_str_dict[s2[l]] == small_str_dict[s2[l]] - 1:
                    matches -= 1
            l += 1

        return matches == len(small_str_dict)













