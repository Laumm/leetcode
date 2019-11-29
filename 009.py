class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        num = x
        result = 0
        while num  > 0  :
            rem = num % 10 
            result = result * 10 + rem
            num = num // 10
        if result == x :
            return True
        return False
            

