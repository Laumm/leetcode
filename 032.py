class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lo=ro=mx= 0 
        pnum = []
        for c in s :
            if c == '(' :
                lo += 1
                if len(pnum) == 0 : pnum.append(1)
                else : pnum.append(pnum[-1] + 1)
                continue
            if lo  > ro :
                ro += 1
                pnum.append(pnum[-1]-1)
                for o in range(ro,0,-1):
                    if pnum[-o * 2] == pnum[-1] + 1 and o * 2  > mx:
                        if min(pnum[-o*2:]) >=   pnum[-o * 2] - 1:
                            mx = o * 2
                continue
            pnum=[]
            lo = ro = 0
        return mx

