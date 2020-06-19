class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            nums.append(target)
            return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                nums.insert(i, target)
                return i