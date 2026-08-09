class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        l = 0
        m = {}
        for c in s1:
            m[c] = m.get(c, 0) + 1
        while r <= len(s2):
            p = {}
            for i in range(l, r):
                p[s2[i]] = p.get(s2[i], 0) + 1 
            if p == m:
                return True
            l += 1
            r += 1
        return False
