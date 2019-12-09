class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = 0 
        if dividend < 0 :
            neg += 1
            dividend = -dividend
        if divisor <0 :
            neg += 1
            divisor = -divisor
        nums = str(dividend)
        div = 0
        mod = 0
        for num in nums :
            num = int(num)
            total = mod * 10 + num
            div = div * 10
            while total >= divisor :
                div += 1
                total =total -divisor
            mod = total
        mx = (1<<31) -1
        mn = -1<<31
        if neg == 1 :
            div = -div
        if div < mn or div > mx :
            return mx
        return div
            







