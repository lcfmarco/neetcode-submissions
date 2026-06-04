class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode the string by using a number, and a hashtag for delimiter
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word

        return res
     
    def decode(self, s: str) -> List[str]:
        
        # Loop through the given string

        res = []

        # Keep track of our current letter
        i = 0

        # While we are still checking our string
        while i < len(s):
            # Attempt j to store our current index
            # We will use j to compare the start of the number, to the end

            j = i

            # Keep shifting up index j until we find the delimiter
            while s[j] != "#":
                j += 1

            # Everything before the delimiter (noted by index i as the start point) is the length
            length = int(s[i : j])

            i = j + 1 + length

            res.append(s[j + 1 : i])

        return res



            

        