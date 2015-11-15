class Solution(object):
    def moveZeroes(self, nums):
        last = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[last] = nums[last], nums[i]
                last += 1

