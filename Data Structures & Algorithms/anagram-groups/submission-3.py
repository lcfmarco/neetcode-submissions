from collections import defaultdict

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # When there is no elements, make it a list
        ana_dict = defaultdict(list)
        
        # Time to process through the string, and make it keys

        for word in strs:
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord('a')] += 1

            ana_dict[tuple(char_count)].append(word)

        return ana_dict.values()

