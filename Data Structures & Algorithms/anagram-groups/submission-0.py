class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for word in strs:
            sorted_str = ''.join(sorted(word))
            if anagram_dict.get(sorted_str,"doesn't exist") == "doesn't exist":
                anagram_dict[sorted_str] = [word]
            else:
                anagram_dict[sorted_str].append(word)
        return list(anagram_dict.values())