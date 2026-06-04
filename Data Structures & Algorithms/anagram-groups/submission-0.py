class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        answer_array = []

        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord('a')] += 1

            key = tuple(letters)



            anagram_dict[key] = anagram_dict.get(key, []) + [word]

        return list(anagram_dict.values())