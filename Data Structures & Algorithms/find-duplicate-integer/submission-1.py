class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        is_visited = {}
        for num in nums:
            if num not in is_visited:
                is_visited[num] = is_visited.get(num , 1)
            else:
                return num
        return -1