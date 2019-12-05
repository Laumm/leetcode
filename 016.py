class Solution:
    def threeSumClosest(self, nums,target) :
        n=len(nums)
        nums.sort()
        diff = nums[0] + nums[1] + nums[2] - target
        mixNum = nums[0] + nums[1] + nums[2]
        if diff < 0 :
            diff = -diff
        for i in range(n-1):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                sm = nums[i] + nums[L] + nums[R]
                if(sm==target):
                    return sm
                elif(sm>target):
                    R=R-1
                    if sm - target < diff :
                        diff = sm - target
                        mixNum = sm
                else:
                    L=L+1
                    if target - sm  < diff :
                        diff = target - sm 
                        mixNum = sm
        return mixNum
s =Solution()
print(s.threeSumClosest([0,2,1,-3],1))
