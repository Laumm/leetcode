class Solution:
    def intToRoman(self, num: int) -> str:
        def oneToRoman(num) :
            # 特殊规则
            if num == 4 :
                return "IV"
            if num == 9 :
                return "IX"
            if num == 40 :
                return "XL"
            if num == 90 :
                return "XC"
            if num == 400 :
                return "CD"
            if num ==  900:
                return "CM"
        
            result = ""
            # 进行转化
            rep = num // 1000
            num = num % 1000
            result += "M" * rep
            # D
            rep = num // 500
            num = num % 500
            result +=  "D" * rep
            # C
            rep = num // 100
            num = num % 100
            result +=  "C" * rep
            # L
            rep = num // 50
            num = num % 50
            result +=  "L" * rep
            # X
            rep = num // 10
            num = num % 10
            result +=  "X" * rep
            # V
            rep = num // 5
            num = num % 5
            result +=  "V" * rep
            # I
            rep = num 
            result +=  "I" * rep
            return result
        n = num // 1000
        num = num % 1000
        result = oneToRoman(n*1000)
        n = num // 100
        num = num % 100
        result +=  oneToRoman(n*100)
        n = num // 10
        num = num % 10
        result +=  oneToRoman(n*10)
        result +=  oneToRoman(num)
        return result

    


