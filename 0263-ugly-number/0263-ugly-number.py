class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n>5:
            if n % 2 == 0:
                n = n/2
                continue
            elif n % 3 == 0:
                n = n/3
                continue
            elif n % 5 == 0:
                n = n/5
                continue
            else:
                return False
        return True