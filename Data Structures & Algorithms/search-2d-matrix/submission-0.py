class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        L_out = 0
        R_out = m - 1
        while L_out <= R_out:
            M_out = L_out + ((R_out - L_out)//2)
            if matrix[M_out][0] <= target <= matrix[M_out][-1]:
                if matrix[M_out][0] == target or matrix[M_out][-1] == target:
                    return True
                L_in = 0
                R_in = n - 1
                while L_in <= R_in:
                    M_in = L_in + ((R_in - L_in)//2)
                    if target == matrix[M_out][M_in]:
                        return True
                    elif target < matrix[M_out][M_in]:
                        R_in = M_in - 1
                    else:
                        L_in = M_in + 1
                return False
            elif target < matrix[M_out][0]:
                R_out = M_out - 1
            elif target > matrix[M_out][-1]:
                L_out = M_out + 1
        return False
                
        