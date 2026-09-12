class Solution:
    def findMin(self, nums: List[int]) -> int:
        newNums = sorted(nums)
        return newNums[0] 