#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_result = self.check_row(board)
        column_result = self.check_column(board)
        grid_result = self.check_subgrid(board)
        #print(row_result, column_result, grid_result)
        return row_result and column_result and grid_result
        
    def check_row(self, board):
        for row in board:
            dic = {i:row.count(i) for i in np.unique(row)}
            for each in dic:
                if each == '.':
                    pass
                elif dic[each] != 1:
                    return False 
        return True
                    
    def check_column(self, board):
        b = []
        for i in range(9):
            lst = []
            for row in board:
                lst.append(row[i])
            b.append(lst)
        return self.check_row(b)
    
    def check_subgrid(self,board):
        result = True
        for i in range(0,9,3):
            for j in range(0,9,3):
                result = result and self.check(board,i,j)
        return result
    
    def check(self, board, i, j):
        lst = []
        for p in range(3):
            for q in range(3):
                lst.append(board[i+p][j+q])
        #print(lst)
        count = []
        for each in lst:
            if each != '.' and each in count:
                return False
            else:
                count.append(each)
        return True
                
                
        
        
        
            
        