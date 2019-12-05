class Solution:
    def fourSum(self, nums, target: int):
        n = len(nums)
        nums.sort()
        rs = []
        print(nums)
        for i in range(n-3):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,n-2):
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue
                L = j + 1 
                R = n-1
                while (L<R):
                    print(i,j,L,R)
                    if nums[i] + nums[j] + nums[L] + nums[R] == target :
                        rs.append([nums[i],nums[j],nums[R],nums[L]])
                        while(L<R and nums[L+1] == nums[L]):
                            L += 1
                        while(L<R and nums[R-1] == nums[R]):
                            R-=1
                        L +=1
                        R -= 1
                    elif nums[i] + nums[j] + nums[L] + nums[R] > target :
                        R -= 1
                    else :
                        L +=1 
                j += 1
            i+=1
        return rs

s =Solution()
print(s.fourSum([-2,0,0,3,3,-1],5))
