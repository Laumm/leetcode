class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        row = {}
        line = {}
        box = {}
        for i in range(9):
            if not row.get(i) :
                row[i] = {'1','2','3','4','5','6','7','8','9'}
            for j in range(9) :
                if not line.get(j) : line[j] = {'1','2','3','4','5','6','7','8','9'}
                bi = (i//3 + 1) * 10 +  (j // 3 + 1) 
                if not box.get(bi) : box[bi] =  {'1','2','3','4','5','6','7','8','9'}
                if board[i][j] == '.' : continue
                row[i].remove(board[i][j])
                line[j].remove(board[i][j])
                box[bi].remove(board[i][j])
        return  self.slove(board,row,line,box)
    def slove(self,board,row,line,box) :
        for i in range(9) :
            for j in range(9) :
                if board[i][j] != '.': continue
                bi = (i//3 + 1) * 10 +  (j // 3 + 1) 
                cs  = row[i]  &  line[j] & box[bi] 
                for c in cs :
                    board[i][j] = c
                    row[i].remove(c)
                    line[j].remove(c)
                    box[bi].remove(c)
                    result = self.slove(board,row,line,box)
                    if result  :
                         return result
                    board[i][j] = '.'
                    row[i].add(c)
                    line[j].add(c)
                    box[bi].add(c)
                return None
        return board
s = Solution()
board =  [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print(s.solveSudoku(board))



