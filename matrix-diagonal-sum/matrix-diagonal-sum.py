class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        length = len(mat)-1
        
        ## add elments of the primary and secondary diagolans
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][length]
            length -= 1
        
        ##if the lenght of mat is odd, subtract the middle number that has been added twice
        if len(mat) % 2 == 1:
            length = len(mat)-1
            sum = sum - mat[length//2][length//2]
            return sum 
        else:
            return sum