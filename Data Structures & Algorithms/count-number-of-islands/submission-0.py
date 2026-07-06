from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        q = deque()
        count = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    seen.add((r,c))
                    q.append((r,c))
                    while q:
                        row,col = q.popleft()
                        for dr,dc in directions:
                            nr,nc = row+dr,col+dc
                            if 0<=nr<len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr,nc) not in seen:
                                seen.add((nr,nc))
                                q.append((nr,nc))
                    count +=1
        return count 
                        