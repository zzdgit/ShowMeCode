

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    for v in range(3, len(nums)):
                        n_sum = nums[i] + nums[i+j] + nums[i+j+k-1] + nums[i+j+k+v-3]
                        if nums == target:
                            result.append(n_sum)
                        if n_sum > target:
                            break
        return result


aa = [1, 0, -1, 0, -2, 2]
target = 0
Solution().fourSum(aa, target)
