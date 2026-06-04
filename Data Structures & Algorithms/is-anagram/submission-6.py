class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict1 = {}
        char_dict2 = {}

        for i in s:
            if i in char_dict1:
                char_dict1[i] += 1
            else:
                char_dict1[i] = 1
            
        for j in t:
            if j in char_dict2:
                char_dict2[j] += 1
            else:
                char_dict2[j] = 1
        
        return char_dict1 == char_dict2

