class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoding some sort of limiter, we can use the number and hash tag combo
        res = ""

        for word in strs:
            length = str(len(word))

            res += length + "#" + word

        return res

    def decode(self, s: str) -> List[str]:

        # Once we face a hashtag, we will get the length
        # From hashtag to the length, take the word and append it to the list

        res = []

        i = 0

        while i < len(s):
            j = i

            while s[i] != "#":
                i += 1

            length = int(s[j:i])

            word = s[i + 1 : i + 1 + length]

            i = i + length + 1

            res.append(word)

        return res

            