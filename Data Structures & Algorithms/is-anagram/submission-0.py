class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()

        for i in list(s):
            if s_dict.get(i,-1) == -1:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for j in list(t):
            if t_dict.get(j,-1) == -1:
                t_dict[j] = 1
            else:
                t_dict[j] += 1

        for k in s_dict.keys():
            if  t_dict.get(k,0) != s_dict[k]:
                return False
    
        return True