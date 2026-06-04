class Solution:
    def encode(self, strs: List[str]) -> str:
        # length, #, word

        res = ""

        for word in strs:
            length = len(word)

            res += str(length) + "#" + word

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = ""
        while i < len(s):
            if s[i] != "#":
                length += s[i]
                i += 1
            else:
                length = int(length)
                res.append(s[i + 1 : i + 1 + length])

                i = i + 1 + length
                length = ""

        return res
