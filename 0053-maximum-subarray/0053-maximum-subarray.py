import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        maxSum = nums[0] 
        currSum = nums[0]
        for r in range(1, len(nums)):
            if nums[r] > currSum + nums[r]:
                l = r
                currSum = nums[r]
            else:
                currSum += nums[r]
            maxSum = max(maxSum,currSum)

        return maxSum


        