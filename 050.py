table = {}
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n in table : return table[n]
        if n == 0 : return 1
        if n == 1 : return x 
        if n == -1 : 
            if x ==0 :return float('inf')
            return 1/x
        mult = -1 if n < 0 else 1
        an = abs(n)
        mid = an // 2
        result =  self.myPow(x,mid * mult) * self.myPow(x,(an-mid) * mult )
        table[n] = result
        return result
s =Solution()
print(s.myPow(2.1000,3))
