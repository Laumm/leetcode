class Solution:
    def findSubstring(self, s: str, words):
        wn = len(words)
        if wn ==  0 :
            return []
        cn = len(words[0])
        if cn == 0 :
            return [i for i in range(len(s)+1)]
        tn = wn * cn 
        wmaps = {}
        rs = []
        for word in words :
            wmaps[word] = wmaps.get(word,0) + 1
        for i in range(len(s) - tn + 1):
            maps = wmaps.copy()
            for j in range(i,i + tn,cn):
                w = s[j:j+cn]
                if w in maps : maps[w] -= 1
                else : break

            sub = True
            for v in maps.values():
                if v != 0 :
                    sub = False
                    break
            if sub :
                rs.append(i)
        return rs















