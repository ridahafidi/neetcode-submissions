class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        m = {}
        l = 0
        r = 0
        length = 0
        while r < len(s):
            if s[r] not in m:
                m[s[r]] = m.get(s[r], 0) + 1
            elif s[r] in m:
                m[s[r]] += 1
            length = (r - l + 1) - max(m.values()) 
            if length <= k:
                res = r - l + 1
            else:
                m[s[l]] -= 1
                l += 1
            r += 1
        return res
