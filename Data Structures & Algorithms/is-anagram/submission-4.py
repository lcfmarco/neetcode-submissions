class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        
        for c in t:
            if c in dict_t:
                dict_t[c] += 1
            else:
                dict_t[c] = 1
        
        s_len = len(s)
        t_len = len(t)

        for char in max(s, t):
            if char not in dict_t or char not in dict_s:
                return False
            elif dict_s[char] != dict_t[char]:
                return False
            
        return True