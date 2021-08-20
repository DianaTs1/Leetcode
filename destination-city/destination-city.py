class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 0:
            return None
        
        edges = {}
        for start, destination in paths:
            edges[start] = destination
            
                
        for start in edges.keys():
            destination = edges.get(start)
            if not edges.get(destination):
                return destination
				
        

        
       