class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        q = deque()

        rows,cols = len(board),len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if r in [0,rows-1] or c in [0,cols-1]:
                    if board[r][c] == "O":
                        seen.add((r,c))
                        q.append((r,c))
                        board[r][c] = "T"

        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc 
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and board[nr][nc] == "O":
                        seen.add((nr,nc))   
                        q.append((nr,nc))
                        board[nr][nc] = "T"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        
