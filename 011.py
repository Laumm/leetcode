class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx  = 0
        l = 0
        r = len(height)
        while l < r :
            mx = max(mx , (r-l) * min(height[l],height[r]))
            if height[l] < height[r]:
                l +=1
            else :
                r -= 1
        return mx
