class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs: 
            encoded_str += str(len(s))
            encoded_str += "#"
            encoded_str += s
        print(encoded_str)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        i = 0
        output_list = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(i,j)
            len_of_word = int(s[i:j])
            i = j + 1
            j = j + len_of_word + 1
            word = s[i:j]
            output_list.append(word)
            i = j
        return output_list