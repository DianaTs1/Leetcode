class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        ## Create new list with maxLen sides for each rectangle      
        maxlen_list = [min(rect) for rect in rectangles]
        
        ## Find the greatest side 
        maxlen = max(maxlen_list)
        
        ## Return the count of rectangles with highest side
        return maxlen_list.count(maxlen)