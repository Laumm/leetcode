class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0 : return []
        n = len(matrix[0])
        if n == 0 : return []

        # 遍历到对角
        up =[] 
        down = []
        for k  in  range(m+n-1):
            j =  k if k < n-1 else n-1
            i = k-j
            up.append(matrix[i][j])
            if j > 0 and i < m-1 :
                j = k if k < m-1 else m-1
                i = k-j
                down.append(matrix[j][i])
        result = up + down[::-1]
        sub_matrix = [ [ matrix[sm][sn] for sn in range(1,n-1) ] for sm in range(1,m-1)   ]
        return  result + self.spiralOrder(sub_matrix)
s = Solution()
print(s.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))






