class Solution:
    def maxSubArray(self, nums):
        mnum = float('-inf')
        stack = []
        for num in nums:
            if num > mnum : mnum = num
            if len(stack) == 0 and num < 0 : continue
            if num >= 0 :
                stack.append(num)
                continue
            stack_total = sum(stack)
            if stack_total > mnum : mnum = stack_total
            if stack_total +  num >= 0 :
                stack.append(num)
            else :
                stack=[]
        if len(stack)  > 0 :
            if sum(stack) > mnum :
                return sum(stack)
        return mnum


