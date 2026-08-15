class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t: #gets all letter in t and their frequency
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity") 
        l = 0
        for r in range(len(s)):
            c = s[r] 
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: #sees if the current letter is in t and if we have the correct frequency
                have += 1 # if so, we have one of our letter completed

            while have == need: # if we have all we need, if we never come in, resLen will be infinity
                if (r - l + 1) < resLen: #see current len and update if smaller
                    res = [l, r] #get first so that we the current substring slice
                    resLen = r - l + 1 

                window[s[l]] -= 1 #we minus 1 because we're moving l to the right by 1 so we lose that letter
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if we move on to a letter that is not in t
                    have -= 1 # we dont have the last letter, but if we dont come in, it's the same letter
                l += 1
        l, r = res #turn [] in ints
        return s[l : r + 1] if resLen != float("infinity") else ""