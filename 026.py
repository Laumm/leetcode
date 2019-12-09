class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        while i < len(nums) :
            if nums[i] == nums[i-1] :
                nums[i-1:] = nums[i:]
                i -= 1
            i += 1
        return len(nums)


