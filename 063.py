class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        pmap = {}
        m = len(obstacleGrid)
        if m == 0 : return 0
        n = len(obstacleGrid[0])
        if n == 0 : return 0 
        for i in range(m):
            for j in range(n):
                paths = 0
                if obstacleGrid[i][j] == 1 :
                    pmap[(i,j)] = paths
                    continue
                if (i,j) == (0,0) :
                    pmap[(i,j)] = 1
                    continue
                if i > 0  :
                    paths += pmap[(i-1,j)]
                if j > 0  :
                    paths += pmap[(i,j-1)]
                pmap[(i,j)] = paths
        return pmap[(m-1,n-1)]

