class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        dic = {}
        for nbr in nums:
            val = target - nbr
            if val in dic:
                return [dic[val], index]
            else:
                dic[nbr] = index
            index += 1