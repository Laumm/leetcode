class Solution:
    def insert(self, intervals, newInterval):
        result = []
        for i in  range(len(intervals)) :
            v = intervals[i]
            # 无重叠
            if v[1] < newInterval[0] : 
                result.append(v)
                continue
            if v[0] > newInterval[1]:
                i -= 1
                break
            newInterval=(min(v[0],newInterval[0]),max(v[1],newInterval[1]))
        result.append(newInterval)
        return result + intervals[i+1:]

