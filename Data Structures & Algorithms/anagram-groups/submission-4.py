class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_dict = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagram_dict[key].append(s)
        
        for anagrams in anagram_dict.values():
            res.append(anagrams)
        return res
