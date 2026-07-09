class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == 2:
                    seen.add((r,c))
                    q.append((r,c,0))
                
        
        time = 0
        while q:
            for _ in range(len(q)):
                row,col,time = q.popleft()
                grid[row][col] = 2
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and grid[nr][nc] != 0:
                        seen.add((nr,nc))
                        q.append((nr,nc,time+1))
            
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time 