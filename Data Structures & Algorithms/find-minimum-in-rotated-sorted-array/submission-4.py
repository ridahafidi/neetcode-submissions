class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotationNbr = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] > nums[j]:
                if nums[j - 1] > nums[j]:
                    return nums[j]
                j -= 1
            else:
                if nums[i + 1] > nums[i]:
                    return nums[i]
                i += 1
        return nums[i]