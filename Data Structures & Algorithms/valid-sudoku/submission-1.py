class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            seen = set()
            for j in range(9):
                if row[j] == ".":
                    continue 
                elif row[j] in seen:
                    return False 
                seen.add(row[j])
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue 
                elif board[j][i] in seen:
                    return False 
                seen.add(board[j][i])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3)*3 + i
                    col = (square % 3)*3 + j 
                    if board[row][col] == ".":
                        continue 
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True 