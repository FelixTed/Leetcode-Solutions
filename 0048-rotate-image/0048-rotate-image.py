class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Transpose
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        # Swap rows 
        columns = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][columns-j-1]
                matrix[i][columns-j-1] = temp
