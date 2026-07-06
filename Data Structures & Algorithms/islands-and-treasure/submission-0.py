from collections import deque
class Solution:
    def findZero(self,start,grid):
        seen = set()
        q = deque()
        q.append((start[0],start[1],0))
        seen.add((start[0],start[1]))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rows,cols = len(grid),len(grid[0])
        while q:
            row,col,level = q.popleft()
            if grid[row][col] == 0:
                return level
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and grid[nr][nc] != -1:
                    seen.add((nr,nc))
                    q.append((nr,nc,level+1))
        return -1
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    pos = self.findZero((r,c),grid)
                    if pos == -1:
                        pos = 2147483647
                    
                    grid[r][c] = pos 
