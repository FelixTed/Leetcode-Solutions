class Solution(object):
    def rob(self, nums):
        robbed = 0
        notRobbed = 0
        for element in nums:
            toRob = notRobbed + element
            notToRob = max(robbed,notRobbed)
            robbed, notRobbed = toRob, notToRob
        return max(robbed,notRobbed) 


        