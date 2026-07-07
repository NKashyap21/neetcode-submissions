from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        rows,cols = len(grid),len(grid[0])

        def addFruit(r,c,time):
            if 0 <= r < rows and 0 <= c < cols and (r,c) not in seen and grid[r][c] != 0:
                seen.add((r,c))
                q.append((r,c,time))


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

                addFruit(row+1,col,time+1)
                addFruit(row-1,col,time+1)
                addFruit(row,col+1,time+1)
                addFruit(row,col-1,time+1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time 