import math
class Solution:
    def getPermutation(self, n,k):
        def  permutation(nums,k):
            n = len(nums)
            if n == 1 : return nums[0]
            factorial = 1
            for i in range(1,n):
               factorial = factorial*i
            index = (k-1) // factorial
            result = nums[index]  +  permutation(nums[:index] + nums[index+1:],k-index * factorial)
            return  result
        nums = [str(i) for i in range(1,n+1)]
        return permutation(nums,k)

s = Solution()
print(s.getPermutation(3,5))
