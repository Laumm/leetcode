class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0 :
            return [-1,-1]
        mid = len(nums) // 2
        if nums[mid] ==target :
            for i in range(mid,-1,-1):
                if nums[i] != target :
                    i += 1
                    break
            for j in range(mid,len(nums)):
                if nums[j] != target :
                    j -= 1
                    break
            return [i,j]
        if nums[mid] > target :
            return self.searchRange(nums[:mid],target)
        result =  self.searchRange(nums[mid+1:],target)
        if result[0] == -1 :
            return result
        return [mid + v + 1 for v in result]

