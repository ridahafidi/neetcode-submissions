class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        i = 0
        for s in strs:
            l = len(s)
            res += str(l)
            res += '\n'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        to_add = ""
        i = 0
        while i < len(s):
            l = 0
            to_add = ""
            if s[i].isdigit():
                nbr = 0
                while s[i].isdigit():
                    nbr = nbr * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                l = nbr
                i += 1
                end = l + i
                while i < end:
                    to_add += s[i]
                    i += 1
            res.append(to_add)
        return res