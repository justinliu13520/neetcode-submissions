class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use a dictionary to keep track of frequency of current minWindow
        # conditions on matches:
        #   Increase if Letter in t and that the frequency is same
        #   decrease if letter in t and frequency is now less than dictionary's
        # need to keep track of min and pointers for slicing


        if len(t) > len(s):
            return ""

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for letter in t:
            t_dict[letter] += 1

        res, min_length = [-1,-1],float("inf")
        l = 0
        have, need = 0, len(t_dict)

        for r in range(len(s)):
            cur_letter = s[r]
            s_dict[cur_letter] += 1
            if cur_letter in t and s_dict[cur_letter] == t_dict[cur_letter]:
                have += 1

            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = [l,r]
                # now that we have a valid window, we try to shrink to get min
                left_letter = s[l]
                s_dict[left_letter] -= 1
                if left_letter in t and s_dict[left_letter] < t_dict[left_letter]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if min_length != float("inf") else ""


        