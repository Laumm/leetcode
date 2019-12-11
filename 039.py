class Solution:
    def combinationSum(self, candidate, target: int) :
        candidate.sort()
        i = 0
        for v in candidate:
            if v > target :
                break
            i += 1 
        if i == 0 :
            return [[]]
        candidate = candidate[:i]
        candidate.reverse()
        return track(candidate,target)

def track(candidate, target):
    result = []
    if len(candidate) == 0  : return result
    base =candidate[0]
    mc = target // base
    for  i in range(mc,-1,-1) :
        diff = target - base  * i 
        if diff == 0 :
            result.append([base] * i)
            continue
        sub_result = track(candidate[1:],diff)
        for sub in sub_result :
            result.append(sub + [base] * i)
    return result 

                



