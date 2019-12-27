class Solution:
    def merge(self, intervals):
        left = []
        right = []
        for v in intervals :
            left.append(v[0])
            right.append(v[1])
        left =sorted(left)
        right=sorted(right)
        stack = []
        i = j = 0
        result = []
        while j < len(right) :
            if i < len(left) and  left[i] <= right[j] :
                stack.append(left[i])
                i += 1
                continue
            e = stack.pop()
            if len(stack) == 0 : 
                result.append([e,right[j]])
            j += 1
        return result
