class Solution:

    def encode(self, strs: List[str]) -> str:    
        # Use a delimiter
        res = ""
        for word in strs:
            length = str(len(word))
            res += length + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i : j])

            j = j + 1
            i = j + length

            res.append(s[j : i])

        return res
        