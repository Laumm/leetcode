class Solution:
    def groupAnagrams(self, strs) :
        def hash(s) :
            return ''.join(sorted(s))
        kv = {}
        for s in strs :
            key = hash(s)
            if key not in  kv :
                kv[key] = []
            kv[key].append(s)
        result = []
        for v in kv.values():
            result.append(v)
        return result 

            
