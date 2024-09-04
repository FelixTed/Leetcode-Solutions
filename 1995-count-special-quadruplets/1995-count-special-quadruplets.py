class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 3
        count = 0
        while i < len(nums):
            j = 0
            x = 1
            z = 2
            while(True):
                if(nums[i] == nums[j]+nums[x]+nums[z]):
                    count += 1
                if z < i-1:
                    z += 1
                elif x < i-2:
                    x += 1
                    z = x+1
                elif j < i-3:
                    j += 1
                    x = j + 1
                    z = x + 1
                else:
                    i += 1
                    break

        return count
                