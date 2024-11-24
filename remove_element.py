class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        copynums =nums[:]
        
        for i in range(len(nums)):
            if not nums[i]==val:
                nums[j]=copynums[i]
                j = j+1
        for i in range(j, len(nums)):
            nums[i] = '_'

        return j

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        