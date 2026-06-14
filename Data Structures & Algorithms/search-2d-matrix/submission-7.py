class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        while top <= bottom:
            m = (top+bottom)//2
            if matrix[m][-1] < target:
                top = m+1
            elif matrix[m][0] > target:
                bottom = m-1
            elif matrix[m][0] <= target <= matrix[m][-1]:
                break
        if not (top<=bottom):
            return False
        
        row = matrix[m]
        l,r = 0,len(row)-1
        while l <= r:
            m = (l+r)//2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m+1
            else:
                r = m-1
        return False