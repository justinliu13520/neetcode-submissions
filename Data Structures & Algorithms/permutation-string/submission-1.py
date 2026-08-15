class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = dict()
        for l in s1:
            s1_dict[l] = s1_dict.get(l,0) + 1
        print(s1_dict)
        begin = 0
        for end in range(len(s1)-1,len(s2)):
            s2_dict = dict()
            print(begin+len(s1))
            for i in range(begin,begin+len(s1)):
                s2_dict[s2[i]] = s2_dict.get(s2[i],0) + 1
            print(s2_dict)
            if s2_dict == s1_dict:
                return True
            begin += 1

        return False