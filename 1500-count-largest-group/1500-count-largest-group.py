class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        for i in range(1,n+1):
            sum = 0
            while(i  > 0):
                sum += i%10
                i = i // 10
            if sum in dic:
                dic[sum] += 1
            else:
                dic[sum] = 1
        maximum = max(dic.values())
        count = 0
        for element in dic:
            if dic[element] == maximum:
                count+=1
        return count
        