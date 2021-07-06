class Solution:
def findCenter(self, edges: List[List[int]]) -> int:
    
    for i in range(1, len(edges)):
        
        if edges[i][0] in edges[i - 1]:
            return edges[i][0]
        else:
            return edges[i][1]
