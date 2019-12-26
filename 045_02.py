class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        step= maxPosition=end =0
        for i in range(n-1):
            maxPosition = max(maxPosition,nums[i] + i)
            if i == end :
                step += 1
                end = maxPosition
        return step



