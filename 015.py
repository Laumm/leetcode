class Solution:
    def threeSum(self, nums):
        vmap = {}
        rs = set()
        # 先排序排序
        nums.sort()
        for i in range(1,len(nums)):
            print(vmap)
            if -nums[i] in vmap:
                for v in vmap[-nums[i]]:
                    rs.add((v[0],v[1],nums[i]))
            for j in range(i) :
                total = nums[i] + nums[j]
                if total not in vmap :
                    vmap[total] = set()
                vmap[total].add((nums[j],nums[i]))
        return rs
s =Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
