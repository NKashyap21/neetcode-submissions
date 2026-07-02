class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        seen = set()

        def dfs(x,y,idx):
            if idx == len(word):
                return True
            
            if x < 0 or x >= m or y < 0 or y >= n or (x,y) in seen or board[x][y] != word[idx]:
                return False
            seen.add((x,y))
            found = False
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if dfs(x+dx,y+dy,idx+1):
                    found = True
                    break
            
            seen.discard((x,y))


            return found
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if dfs(x,y,0):
                        return True
        
        return False
            