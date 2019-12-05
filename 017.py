class Solution:
    def letterCombinations(self, digits: str) :
        if digits == "" :
            return []
        rs =['']
        mp = {
                "2" :"abc",
                "3" :"def",
                "4" :"ghi",
                "5" :"jkl",
                "6" :"mno",
                "7" :"pqrs",
                "8" :"tuv",
                "9" :"wxyz",
                }
        for d in digits :
            cs = mp[d]
            ns = []
            for v in rs :
                for c in cs :
                    ns.append(v + c)
            rs = ns
        return  rs
