class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n  = sorted(n)
        mid = (len(n) - 1) / 2
        if (len(n) - 1) % 2 == 0:
            return n[int(mid)]
        else:
            a = int(mid)
            b = a + 1
            return (n[b] + n[a]) / 2