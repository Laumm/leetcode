class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0 :
            return -1
        n =len(nums)
        mid = nums[n//2]
        if mid == target :
            return n//2
        offset = 0
        if  mid > nums[-1]  :
            if target >= nums[0] and target < mid :
                toSearch = nums[:n//2]
            else :
                offset = n//2 + 1 
                toSearch = nums[n//2+1 :]
        else  : 
            if target > mid and target <= nums[-1] :
                offset = n//2 + 1 
                toSearch = nums[n//2+1 :]
            else :
                toSearch = nums[:n//2]

        ro = self.search(toSearch,target)
        return offset + ro if ro > -1 else -1 

