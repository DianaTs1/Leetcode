class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        
        for sub_list in grid:
            for elem in sub_list:
                if elem < 0:
                    result +=1
        
        return result