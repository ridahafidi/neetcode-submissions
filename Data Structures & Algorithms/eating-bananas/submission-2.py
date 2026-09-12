class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                # k works, but maybe there is a smaller one
                right = k
            else:
                # k is too slow
                left = k + 1

        return left