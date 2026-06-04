class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointA = 0
        pointB = len(s) - 1

        while pointA <= pointB:
            if not self.isAlphaNum(s[pointA]) and pointA <= len(s):
                pointA += 1
            elif not self.isAlphaNum(s[pointB]) and pointB >= 0:
                pointB -= 1
            else:
                if s[pointA].lower() != s[pointB].lower():
                    return False
                
                pointA += 1
                pointB -= 1
        return True

                

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or \
                (ord("a") <= ord(c) <= ord("z")) or \
                (ord("0") <= ord(c) <= ord("9"))