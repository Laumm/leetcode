class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = 0
        sub = ""
        while strs :
            ix = ''
            for s in strs :
                if len(s) < i+1:
                    return sub
                if len(ix) == 0 :
                    ix = s[i]
                if ix != s[i] :
                    return sub
            i += 1
            sub += ix
        return sub
                

