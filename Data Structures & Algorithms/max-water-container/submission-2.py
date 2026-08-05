class Solution:
    def maxArea(self, heights: List[int]) -> int:
        v = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if v == 0:
                v = min(heights[l], heights[r]) * (r - l)
            else:
                next_v = min(heights[l], heights[r]) * (r - l)
                if v < next_v:
                    v = next_v
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return v
