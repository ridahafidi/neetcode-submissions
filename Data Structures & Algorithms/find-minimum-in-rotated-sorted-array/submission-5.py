class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] > nums[j]:
                i += 1
            else:
                j -= 1
        return nums[i]
            