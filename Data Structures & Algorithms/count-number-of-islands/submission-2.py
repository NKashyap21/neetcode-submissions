class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        q = deque()

        rows,cols = len(grid),len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if not (r,c) in seen and grid[r][c] == '1':
                    seen.add((r,c))
                    q.append((r,c))
                    while q:
                        row,col = q.popleft()
                        for dr,dc in directions:
                            nr,nc = row+dr,col+dc
                            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and grid[nr][nc] == "1":
                                seen.add((nr,nc))
                                q.append((nr,nc))
                    count += 1
        
        return count 