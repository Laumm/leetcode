class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        result = ''
        for i2 in range(n2):
            in_result = 0 
            for i1 in range(n1):
                in_result *= 10
                in_result += int(num1[i1]) *int(num2[i2])
            if len(result) > 0 :result += '0'
            result = strAdd(result, str(in_result))
        return result

# 字符串相加
# 八位相加 ，整数肯定不会溢出
def strAdd(num1,num2) :
    # 补齐相同位数 , 简化处理
    n1 ,n2 = len(num1),len(num2)
    mx = max(n1 ,n2)
    if n1 < mx : num1 = '0' * (mx-n1) + num1
    if n2 < mx : num2 = '0' * (mx-n2) + num2
    result = ''
    step = 8
    base = 10 ** step
    i = mx
    add = 0
    for i in range(mx-step,-1,-step):
        total = int(num1[i:i+step]) + int(num2[i:i+step]) + add 
        if total >  base:
            add = 1 
            in_result = str(total)[1:]
        else :
            add = 0
            in_result = str(total+base)[1:]
        result =   in_result + result
    # 剩余数字相加
    if i > 0  : 
        in_result= (int(num1[:i]) +  int(num2[:i] ) + add )
        result =  str(in_result) + result
        add =0 
    if add >0 :
        result = result + '1'
    return result

s =Solution()
a="4986379436526147432469958204718329158211863797453691789509292244161982290580525007195048267692"
b= "2044896994719"
print(s.multiply(a,b))


