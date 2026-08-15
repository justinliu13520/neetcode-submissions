class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #if key doesn't exist, makes an empty list for value and key given

        for word in strs:
            freq = [0]*26
            for letter in word:
                freq[ord(letter)-ord('a')] += 1 # ord turns into an ascii
            result[tuple(freq)].append(word)
        return list(result.values())