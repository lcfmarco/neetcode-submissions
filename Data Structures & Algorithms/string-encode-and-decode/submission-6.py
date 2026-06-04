class Solution:

    # Way of encoding
        # We need to know the length of the string
        # We also need to have some form of delimiter, a way to know when we are done with the string, or the count of the string
    # We can use a length of number + #
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word

        
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        l, r = 0, 1

        while r < len(s):

            length = ""

            while s[l] != "#":
                length += s[l]
                l += 1


            length = int(length)


            r = l + 1 + length
            word = s[l + 1 : r]

            res.append(word)

            l = r

        return res