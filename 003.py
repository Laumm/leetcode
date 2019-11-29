class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {}
        begin = 0
        max_len =0 
        for i,v in enumerate(s):
            if v not in mp :
                mp[v] = i
                continue
            if mp[v] < begin :
                mp[v] = i
                continue
            s_len = i -begin 
            if s_len > max_len :
                max_len =s_len
            begin = mp[v] + 1
            mp[v] = i    
        
        if len(s)-begin > max_len:
            max_len =len(s)-begin
        return max_len
