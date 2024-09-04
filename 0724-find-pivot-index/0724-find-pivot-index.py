class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum1 = [0]
        prefixSum2 = [0]
        lastIndex = len(nums) - 1

        for i in range(0, len(nums)):
            prefixSum1.append(prefixSum1[i] + nums[i])
            prefixSum2.insert(0, prefixSum2[0] + nums[lastIndex - i])

        for i in range(0,len(prefixSum1)-1):
            if prefixSum1[i] == prefixSum2[i+1]:
                return i
        return -1