class Solution:

    def encode(self, strs: List[str]) -> str:
        #  length#word because the length will allow us to grab the word after the #
        msg = ""
        for word in strs:
            msg += str(len(word)) + "#" + word
        return msg

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i            
            for letter in s:
                if s[j] != "#":
                    j += 1
            len_of_word = int(s[i:j])
            i = j + 1
            j = i + len_of_word
            result.append(s[i:j])
            i = j
        return result
            