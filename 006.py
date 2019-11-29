class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 :
            return s
        cmap = {}
        inc = 0
        for i,v in  enumerate(s) :
            if (i + inc   + 1) % numRows == 0 :
                inc += 1
            quo = (i + inc)  // numRows
            rem = (i + inc)  % numRows
            if quo % 2 == 0 :
                row = rem 
            else :
                row = numRows - rem - 1 
            if row not in cmap :
                cmap[row] = ''
            cmap[row] += v
        result =''
        for key in cmap:
            result += cmap[key]
        return result
