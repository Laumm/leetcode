class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==  1:
            return "1"
        says  =  self.countAndSay(n-1)
        result = ""
        i = b =  0
        for i in range(1,len(says)) :
            if says[i] != says[i-1] :
                result += str(i-b) + says[i-1]
                b = i 
        result += str(i-b + 1) + says[i]
        return result


