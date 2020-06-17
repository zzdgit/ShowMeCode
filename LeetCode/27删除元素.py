# 方法一： 单（双）指针，这里是单指针，当指针等于数组长度，循环结束，数组元素等于给定元素，删除数组中的元素，还指向单前位置，否则指针指向下一个元素
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i = i + 1
        return i + 1


# 方法二： 因为数组中元素，删除后，导致数组中元素所以变化，所从后面循环

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                nums.pop(i)
        return len(nums)