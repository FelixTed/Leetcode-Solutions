class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        minRow = set()

        for i in range(len(matrix)):
            currMin = matrix[i][0]
            for j in range(1,len(matrix[0])):
                if matrix[i][j] < currMin:
                    currMin = matrix[i][j] 
            minRow.add(currMin)

        for j in range(len(matrix[0])):
            currMax = matrix[0][j]
            for i in range(1, len(matrix)):
                if matrix[i][j] > currMax:
                    currMax = matrix[i][j]
            if currMax in minRow:
                res.append(currMax)

        return res
