class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pa,at = set(),set()
        seen = set()
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rows,cols = len(heights),len(heights[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    seen.add((r,c))
                    pa.add((r,c))
                    q.append((r,c))
        
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and heights[nr][nc] >= heights[row][col]:
                    seen.add((nr,nc))
                    pa.add((nr,nc))
                    q.append((nr,nc))

        seen = set()
        for r in range(rows):
            for c in range(cols):
                if r == rows-1 or c == cols-1:
                    seen.add((r,c))
                    at.add((r,c))
                    q.append((r,c))
        
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and heights[nr][nc] >= heights[row][col]:
                    seen.add((nr,nc))
                    at.add((nr,nc))
                    q.append((nr,nc))

        z = list(pa.intersection(at))
        res = [list(x) for x in z]
        return res 
        
        
