class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            n = len(image)
            m = len(image[0])
            vis = [[0 for i in range(m)] for j in range(n)]
            dirs = [(0,1),(-1,0),(1,0),(0,-1)]
            original = image[sr][sc]
            image[sr][sc] = newColor    
            q = [(sr,sc)]
            vis[sr][sc]=1
            while len(q):
                i,j = q.pop(0)

                for d in dirs:
                    x,y = i+d[0],j+d[1]
                    if x>=0 and x<n and y>=0 and y<m and image[x][y]==original and not vis[x][y]:
                        q.append((x,y))
                        vis[x][y] =1
                        image[x][y] = newColor
            return image
