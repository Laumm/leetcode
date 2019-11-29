max = (1<<31) - 1
min = (-1<<31)
class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0 :
            return 0
        nums = []
        first = True
        neg = False
        for s in str :
            if first :
                if s == " " :
                    continue
                first = False
                if s == "-" :
                    neg = True
                    continue
                if s == "+"  :
                    continue
                if s >= "0" and s <= "9" :
                    nums.append(s)
                    continue
                return 0
            if s >= "0" and s <= "9" :
                nums.append(s)
            else :
                break
        result  = 0
        for num in nums :
            num = int(num)
            if  not neg  :
                if  (max - num ) / 10 >= result:
                    result = result * 10 + num
                    continue
                return max
            if neg :
                if (-min - num ) / 10 >= result :
                    result = result * 10 + num
                    continue
                return min
        if neg :
            return -1 * result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("           -2147483649"))
