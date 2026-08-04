class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(0, len(nums)):
            j = 0
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return ([i ,j])
                j += 1
            i += 1
        return [0, 0]