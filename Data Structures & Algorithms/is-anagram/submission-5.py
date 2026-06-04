class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for c in range(len(s)):
            dict_s[s[c]] = 1 + dict_s.get(s[c], 0)
            dict_t[t[c]] = 1 + dict_t.get(t[c], 0)
        
        for char in dict_s:
            if dict_s[char] != dict_t.get(char, 0):
                return False
        return True