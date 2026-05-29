class Solution:
    def hasDuplicate(self,arr):
        arr = tuple(arr)
        seen = set()
        for num in arr:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if row is valid
        for i in range(len(board)):
            row = board[i]
            row_num = [int(char) for char in row if char.isalnum()]
            if self.hasDuplicate(row_num):
                return False

        #check if column is valid
        for i in range(len(board[0])):
            column = []
            for j in range(len(board)):
                column.append(board[j][i])
            column_num = [int(char) for char in column if char.isalnum()]
            if self.hasDuplicate(column_num):
                return False

        blocks = [[board[r + i][c + j] for i in range(3) for j in range(3)]for r in range(0, 9, 3)for c in range(0, 9, 3)]

        for block in blocks:
            block_num = [int(char) for char in block if char.isalnum()]
            if self.hasDuplicate(block_num):
                return False
        return True 



