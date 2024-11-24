class Solution(object):
    def removeDuplicates(self, nums):
        setlist = set(nums)
        listlist = list(setlist)
        listlist.sort()
        prelength = len(nums)
        uniquelength = len(listlist)
        salength = prelength-uniquelength
        for i in range(uniquelength):
            nums[i] = listlist[i]
        for i in range(salength):
            nums[uniquelength + i] = '_'

        return uniquelength
        """
        :type nums: List[int]
        :rtype: int
        """
        