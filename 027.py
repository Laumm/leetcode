class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val :
                nums[i:] = nums[i+1:]
                i-=1
            i +=1
        return i

