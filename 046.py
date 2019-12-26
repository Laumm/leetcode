class Solution:
    def permute(self, nums) :
        result = []
        if len(nums) == 0 :
            return result
        for i in range(len(nums)) :
            sub_results = self.permute(nums[:i]+nums[i+1:])
            if len(sub_results) == 0 :
                result.append([nums[i]])
                continue
            for sr in sub_results :
                result.append([nums[i]]+sr)
        return result



