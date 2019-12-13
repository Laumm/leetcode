class Solution:
    def trap(self, heights) -> int:
        contain = 0 
        for i in range(1,len(heights)) :
            top = 0 
            for j in range(i-1,-1,-1):
                if heights[j] <= top :
                    continue
                contain +=  (i-j - 1) * (min(heights[j],heights[i]) - top)
                if heights[j]  >= heights[i]:
                    break
                top = heights[j]
        return contain
