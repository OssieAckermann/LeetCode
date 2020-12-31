#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lst2 = []
        for i in range(len(matrix)):
            lst1 = []
            for each_lst in matrix:
                lst1.append(each_lst[i])
            lst1.reverse()
            lst2.append(lst1)
        for i in range(len(lst2)):
            matrix[i] = lst2[i]
            
            
            