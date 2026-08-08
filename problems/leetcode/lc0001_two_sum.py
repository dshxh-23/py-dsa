class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            if (target-num) in nums[i+1:]:
                nums.remove(num)
                return [i, nums.index(target-num)+1]