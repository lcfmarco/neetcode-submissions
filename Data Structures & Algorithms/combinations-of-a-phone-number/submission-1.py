class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        if digits == "":
            return res
        
        def dfs(pos, combo):
            if pos >= len(digits):
                res.append(combo)
                return

            letters = phone[digits[pos]]

            for letter in letters:
                dfs(pos + 1, combo + letter)

            return

        dfs(0, "")

        return res


            