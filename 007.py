class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = (1 << 31)  - 1 
        min = (-1 <<  31)
        neg = False
        if x  < 0  :
            neg = True
        result = 0
        while True :
            rem  = x % 10 
            if neg  and rem > 0  :
                rem = rem -10 
            x = (x - rem ) // 10 
            # 放置数值移除 max >= result * 10 + rem >= mix 
            #  (max -rem) / 10 >= result >= (mix -rem) / 10 
            if  (max -rem ) / 10 >= result >= (min-rem) / 10 :
                result = result * 10 + rem 
            else :
                return 0 
            if x == 0 :
                return result 

if __name__ == '__main__' :
    s  = Solution()
    print(s.reverse(-1563847412))
