# ����һ�� ����˫��ָ�룬�����ǵ�ָ�룬��ָ��������鳤�ȣ�ѭ������������Ԫ�ص��ڸ���Ԫ�أ�ɾ�������е�Ԫ�أ���ָ��ǰλ�ã�����ָ��ָ����һ��Ԫ��
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


# �������� ��Ϊ������Ԫ�أ�ɾ���󣬵���������Ԫ�����Ա仯�����Ӻ���ѭ��

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