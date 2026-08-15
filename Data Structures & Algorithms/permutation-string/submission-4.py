class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        first_word_dict = defaultdict(int)
        second_word_dict = defaultdict(int)

        for i in range(len(s1)):
            first_word_dict[s1[i]] += 1
            second_word_dict[s2[i]] += 1

        for letter in first_word_dict.keys():
            matches += 1 if first_word_dict[letter] == second_word_dict.get(letter,0) else 0

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == len(first_word_dict):
                return True

            second_word_dict[s2[r]] += 1
            if s2[r] in first_word_dict:
                if second_word_dict[s2[r]] == first_word_dict[s2[r]]:
                    matches += 1
                elif second_word_dict[s2[r]] == first_word_dict[s2[r]] + 1:
                    matches -= 1

            second_word_dict[s2[l]] -= 1
            if s2[l] in first_word_dict:
                if second_word_dict[s2[l]] == first_word_dict[s2[l]]:
                    matches += 1
                elif second_word_dict[s2[l]] == first_word_dict[s2[l]] - 1:
                    matches -= 1
            l += 1

        return matches == len(first_word_dict)
            


        
