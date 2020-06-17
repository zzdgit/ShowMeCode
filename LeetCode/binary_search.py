
def binary_search(alist, num):
    left = 0
    right = len(alist) - 1
    if num > alist[right] or num < alist[left]:
        return None
    while left <= right:
        mid = (right + left) // 2
        if alist[mid] < num:
            left = mid + 1
        elif alist[mid] > num:
            right = mid - 1
        else:
            return num
    return None



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return None
        for i in range(len(nums)//2 + 1):
            num1 = nums[i]
            num2 = target - num1
            num3 = self.binary_search(nums, num2)
            if num3:
                return[num1, num3]
            else:
                return None
    def binary_search(self, alist, num):
        left = 0
        right = len(alist) - 1
        while left <= right:
            mid = (right + left) // 2
            if alist[mid] < num:
                left = mid + 1
            elif alist[mid] > num:
                right = mid - 1
            else:
                return num
        return None

if __name__ == "__main__":
    alist = [2, 4, 7, 24, 43, 111, 231]
    alist = [16,16,18,24,30,32]
    # print(binary_search(alist, 32))
    print(Solution().twoSum(alist, 48))
