class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        i = 0
        for v in candidates:
            if v > target :
                break
            i += 1 
        if i == 0 :
            return []
        candidates = candidates[:i]
        candidates.reverse()
        return track(candidates,target)

def track(candidate, target):
    result = set()
    if len(candidate) == 0  : return result
    base =candidate[0]
    mc = 1 if target >= base else 0
    for  i in range(mc,-1,-1) :
        diff = target - base  * i 
        if diff == 0 :
            result.add((base,) * i)
            continue
        sub_result = track(candidate[1:],diff)
        for sub in sub_result :
            result.add(sub + (base,) * i)
    return result 

