class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 对角互换
        for i in range(n):
            for j in range(i):
                matrix[i][j] ,matrix[j][i] = matrix[j][i],matrix[i][j]
        # 行反转
        def revert(nums) :
            for i in range(len(nums)//2):
                nums[i],nums[-i-1] = nums[-i-1],nums[i]
            return 
        for line in matrix:
            revert(line)
        return 

                
                    



