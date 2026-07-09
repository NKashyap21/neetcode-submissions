class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        maxArea = 0

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rows,cols = len(grid),len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == 1:
                    seen.add((r,c))
                    q.append((r,c))
                    area = 1
                    while q:
                        row,col = q.popleft()
                        for dr,dc in directions:
                            nr,nc = row+dr,col+dc
                            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and grid[nr][nc]==1:
                                seen.add((nr,nc))
                                q.append((nr,nc))
                                area += 1
                    maxArea = max(maxArea,area)
        return maxArea