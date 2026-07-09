class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()

        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    q.append((r,c))
        
        dist = 1
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr,nc = row+dr,col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and grid[nr][nc] != -1:
                        seen.add((nr,nc))
                        q.append((nr,nc))
                        grid[nr][nc] = dist
            dist += 1

                    