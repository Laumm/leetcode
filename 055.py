class Solution:
    def canJump(self, nums):
        n = len(nums)
        if n == 1: return True
        ms = 1
        for i in range(n):
            ms = ms -1 
            if nums[i] > 0 :
                ms = max(ms,nums[i])
                continue
            # nums = 0
            if ms ==  0 :
                if i == n-1 :return True
                return False
        return True



