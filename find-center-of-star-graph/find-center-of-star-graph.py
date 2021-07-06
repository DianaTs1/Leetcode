class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        new_list = edges[0]+edges[1]
        for elem in new_list:
            if new_list.count(elem) == 2:
                return elem