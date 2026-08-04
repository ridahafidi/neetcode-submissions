class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        ret = []
        for nbr in nums:
            res[nbr] = res.get(nbr, 0) + 1
        i = 0
        x = None
        for i in range(0, k):
            biggest = 0
            for n in res:
                if biggest < res[n]: 
                    biggest = res[n]
                    x = n
            ret.append(x)
            res.pop(x, None)
            i += 1
        if len(ret) == 0:
            return nums
        return ret