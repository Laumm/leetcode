class Solution:
    def permuteUnique(self, nums):
        nums=sorted(nums)
        return  self.permute(nums)
    def permute(self, nums) :
        result = []
        if len(nums) == 0 :
            return result
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i-1] :
                continue
            sub_results = self.permute(nums[:i]+nums[i+1:])
            if len(sub_results) == 0 :
                result.append([nums[i]])
                continue
            for sr in sub_results :
                result.append([nums[i]]+sr)
        return result


