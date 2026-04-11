from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: #获取一个网格
        if not grid: #读取网格尺寸
            rows,cols = 0,0
        else:
            rows = len(grid)
            cols = len(grid[0])
        islands = 0 
        visited = [[False]*cols for _ in range(rows)]#创建一个布尔值队列防止BFS冲突
        def bfs(r,c): #调用BFS       
            queue = deque()
            queue.append((r,c))
            visited[r][c] = True
            while queue : #带搜索队列不为空
                x,y = queue.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append((nx,ny))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands += 1
                    bfs(i,j)
        return islands    
