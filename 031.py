class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1,-1,-1):
            finish = False
            for j in range(n-1,i,-1) :
                if nums[i] < nums[j] :
                    nums[i], nums[j] = nums[j],nums[i]
                    finish = True
                    break
            if finish: 
                i += 1
                break
        for j in range((n-i) // 2) :
            nums[i+j],nums[-j-1] = nums[-j-1],nums[i+j]
        return 



