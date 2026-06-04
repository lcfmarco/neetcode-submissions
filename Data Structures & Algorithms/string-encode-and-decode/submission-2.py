class Solution:
    # Encoding: take all strings and split it into one big string
    # Use a limiter (length + #)

    # Decoding: When it detects a number, traverse until it sees a #
        # When a # is found, take the number we found previously, and append that into the list
        # Move on after

    def encode(self, strs: List[str]) -> str:
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

            while s[j] != '#':
                j += 1
            
            length = int(s[i : j])

            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res
        

        