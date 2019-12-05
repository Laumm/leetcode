class Solution:
    def generateParenthesis(self, n: int):
        def insert(ln,rn,ci,ds):
            rs = set()
            if ln == 0 and  rn == 0 :
                return ds
            if ln > 0 and  ( len(ci) == 0 or '(' in ci) :
                ms = set()
                for v in ds :
                    ms.add(v+'(')
                rs = rs |insert(ln-1,rn,ci+'(',ms)
            if rn > 0 and len(ci) > 0 and '(' == ci[-1]:
                ms = set()
                for v in ds :
                    ms.add(v+')')
                rs = rs | insert(ln,rn-1,ci[:-1],ms)
            return rs
        ln=rn=n
        ds={'',}
        return insert(ln,rn,'',ds)



s =Solution()
print(s.generateParenthesis(4))
