class Solution:
    def generateMatrix(self, n: int) :
        matrix = [[ 0  for i in range(n) ] for i in range(n) ]
        box_matrix = []
        box_matrix.append([ 1 for i in range(n+2) ])
        for line in matrix :
            box_matrix.append([1] + line + [1] )
        box_matrix.append([ 1 for i in range(n+2) ])
        

        # ty 移动类型 1-> -1 <- 2 down -2 up
        ty = 1 
        i = j = 1
        num = 0
        while True :
            num += 1
            matrix[i-1][j-1] = num
            box_matrix[i][j] = num
            if ty == 1 :
                if box_matrix[i][j+1] ==0 : j +=1 ; continue
                if box_matrix[i+1][j] == 0 : ty = 2 ; i += 1 ; continue
                break
            if ty == 2 :
                if box_matrix[i+1][j] ==0 : i += 1  ; continue
                if box_matrix[i][j-1] == 0 : ty = -1 ; j -= 1 ; continue
                break
            if ty == -1 :
                if box_matrix[i][j-1] ==0 : j-= 1  ; continue
                if box_matrix[i-1][j] == 0 : ty = -2 ; i -= 1 ; continue
                break
            if ty == -2 :
                if box_matrix[i-1][j] ==0 : i -= 1  ; continue
                if box_matrix[i][j+1] == 0 : ty = 1 ; j += 1 ; continue
                break
        return matrix








