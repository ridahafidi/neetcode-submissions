class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:


            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r

            if target < nums[r]:
                l += 1

            else:
                r -= 1

        return -1