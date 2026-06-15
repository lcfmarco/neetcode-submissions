class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def palindrome_check(part):
            return part == part[::-1]

        def dfs(start):
            if start == len(s):
                res.append(curr.copy())
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]

                if palindrome_check(part):
                    curr.append(part)

                    dfs(end + 1)

                    curr.pop()

        dfs(0)

        return res
