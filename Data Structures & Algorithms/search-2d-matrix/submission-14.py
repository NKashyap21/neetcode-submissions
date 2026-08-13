class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False 
        l,r = 0,len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if target == matrix[m][0]:
                return True 
            elif target < matrix[m][0]:
                r = m -1
            else:
                l = m+1
        row = matrix[r]
        l,r = 0,len(row)-1
        while l <= r:
            m = (l+r)//2
            if row[m] == target:
                return True 
            elif row[m] < target:
                l = m+ 1
            else:
                r = m-1
        return False 