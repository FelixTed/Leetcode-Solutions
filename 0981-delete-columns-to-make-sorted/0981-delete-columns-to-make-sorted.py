class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if len(strs) == 1:
                return 0
        count = 0
        lines = len(strs)
        columns = len(strs[0])
        for i in range(columns):
                temp = [element[i] for element in strs]
                if temp != sorted(temp):
                        count += 1
        return count