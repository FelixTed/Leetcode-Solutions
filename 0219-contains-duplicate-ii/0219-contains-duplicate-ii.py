class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashSet = set([nums[0]])
        if k == 0:
            return False
        l = 0
        h = 1
        while h < len(nums):
            if nums[h] in hashSet and h - l <= k:
                return True
            elif h-l > k:
                hashSet.remove(nums[l])
                l+=1
            elif nums[h] not in hashSet:
                hashSet.add(nums[h])
                h+=1
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        