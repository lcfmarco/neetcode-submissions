class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length)
            res += "#"
            res += word
        return res
    
    
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        length = ""

        while i < len(s):

            if s[i] != "#":
                length += s[i]

                i += 1

                continue
            
            else:
                res.append(s[i + 1: i + 1 + int(length)])

                i = i + 1 + int(length)
            
                length = ""

        return res