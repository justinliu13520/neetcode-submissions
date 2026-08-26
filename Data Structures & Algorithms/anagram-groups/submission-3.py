class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            letters = ''.join(sorted(s))
            anagram_dict[letters].append(s)
        res = []
        for ana in anagram_dict.values():
            res.append(ana)
        return res