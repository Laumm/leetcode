class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 :
            return ''
        result = s[0]
        for i ,v  in enumerate(s) :
            e=i
            same =True
            j = 1 
            while True :
                if e + j > len(s) -1:
                    break
                if same and s[e+j] ==v :
                    e = e+j
                    if e-i  + 1>=  len(result):
                        result = s[i:e+1]
                    continue
                else :
                    same =False
                if i-j < 0 :
                    break
                
                if s[i-j] == s[e+ j] :
                    if  2*j +e-i + 1  >=  len(result) : 
                        result = s[i-j:e+j+1]
                    j += 1
                    continue
                break
        return result       
