class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        for j in range(1, len(nums)):
            if nums[count] != nums[j]:
                count = count + 1
                nums[count] = nums[j]
        return count + 1