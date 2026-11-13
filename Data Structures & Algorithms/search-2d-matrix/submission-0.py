class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        rtop, rbottom = 0, R - 1
        while rtop <= rbottom:
            rmid = (rtop + rbottom) // 2
            if matrix[rmid][-1] < target:
                rtop += 1
            elif matrix[rmid][0] > target:
                rbottom -= 1
            else:
                break
        
        if rtop > rbottom:
            return False
        
        l, r = 0, len(matrix[rmid]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[rmid][m] < target:
                l = m + 1
            elif matrix[rmid][m] > target:
                r = m - 1
            elif matrix[rmid][m] == target:
                return True
        return False
