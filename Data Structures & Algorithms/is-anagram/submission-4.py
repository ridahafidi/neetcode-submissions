class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for key in s:
            dic_s[key] = dic_s.get(key, 0) + 1
        for key in t:
            dic_t[key] = dic_t.get(key, 0) + 1
        if len(dic_s) != len(dic_t):
            return False 
        for k in dic_s:
            for ke in dic_t:
                if k == ke:
                    v = dic_s[k] - dic_t[ke]
                    dic_s.update({k: v})
                    dic_t.update({ke: v})
                    if dic_s[k] != 0:
                        return False
        for k in dic_s:
            if dic_s[k] != 0:
                return False
        for k in dic_t:
            if dic_t[k] != 0:
                return False
        return True
