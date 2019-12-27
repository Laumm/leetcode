class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wl = 0
        for c in s[::-1]:
            if c == ' ' :
                if wl == 0 : continue
                else : break
            wl += 1
        return wl
