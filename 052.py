class Solution:
    def totalNQueens(self, n: int) -> int:
        all_result = []
        squares = [ [ '.' for i in range(n) ] for i in range(n) ]
        can_play = [  (i,j) for i in range(n) for j in range(n) ]
        def slove(squares,can_play,remain) :
            if remain == 0 :  # 放完了
                all_result.append([''.join(v) for v in squares])
                return 
            if len(can_play) == 0 : return   # 不能放了
            for v in can_play :
                if v[0] != n-remain : continue
                squares[v[0]][v[1]] = 'Q'
                not_play = []
                # O(n^2)
                for i in range(n) :
                    for j in range(n) :
                        if i == v[0] or  j == v[1] or (j-i) == (v[1] - v[0]) or (i + j ) == (v[0] + v[1])   :
                            not_play.append((i,j))
                slove(squares,[v for v in can_play if v not in not_play],remain-1)
                squares[v[0]][v[1]] = '.'
            return None
        slove(squares,can_play,n)
        return len(all_result)
