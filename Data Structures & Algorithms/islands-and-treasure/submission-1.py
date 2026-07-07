from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()
        rows,cols = len(grid),len(grid[0])

        def addRoom(r,c):
            if 0 <= r < rows and 0 <= c < cols and (r,c) not in seen and grid[r][c] != -1:
                seen.add((r,c))
                q.append((r,c))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    q.append((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = dist

                addRoom(row+1,col)
                addRoom(row-1,col)
                addRoom(row,col+1)
                addRoom(row,col-1)

            dist += 1

