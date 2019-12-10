class Solution:
    def searchInsert(self, nums, target) -> int:
        i = -1
        for i in range(len(nums)) :
            if nums[i] >=  target :
                return  i 
        return i+1
