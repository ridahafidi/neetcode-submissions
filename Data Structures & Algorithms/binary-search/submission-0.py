class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        if target not in nums:
            return -1
        while i < len(nums):
            if target == nums[i]:
                break
            elif target < nums[i]:
                i -= 1
            elif target > nums[i]:
                i += 1
        return i