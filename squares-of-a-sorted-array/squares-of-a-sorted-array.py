class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        for elem in nums:
            elem = elem * elem
            res.append(elem)
            
        res.sort()
        
        return res