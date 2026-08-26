class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            len_of_s = len(s)
            encoding += str(len_of_s) + "#" + s
        return encoding
    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        right = 0
        while right < len(s):
            while s[right].isdigit():
                right += 1
            length_of_word = int(s[left:right])
            right = right + 1
            res.append(s[right:right+length_of_word])
            left = right+length_of_word
            right = left
        return res