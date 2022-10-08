class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        m,n = len(grid), len(grid[0])
        
        oranges = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    oranges.add((i,j))
                    
                    
        time = 0
        visited = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            i,j, time = q.popleft()
            visited.add((i,j))
            for dx,dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y]==1:
                    grid[x][y]=2
                    if (x,y) in oranges:
                        oranges.remove((x,y))
                    q.append((x,y, time+1))
                    
        return -1 if len(oranges)>0 else time