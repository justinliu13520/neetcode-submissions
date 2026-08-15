class Solution:
    def isPalindrome(self, s: str) -> bool:
        length_of_s = len(s)
        if length_of_s == 0 or length_of_s == 1:
            return True
        maybe_pal = "".join([char if char.isalnum() else "" for char in s.lower()])
        print(maybe_pal)
        if len(maybe_pal) % 2 == 0:
            return True if maybe_pal[:len(maybe_pal)//2] == maybe_pal[len(maybe_pal)-1:len(maybe_pal)//2-1:-1] else False
        return True if maybe_pal[:len(maybe_pal)//2] == maybe_pal[len(maybe_pal)-1:len(maybe_pal)//2:-1] else False


        # abbc abba abbba