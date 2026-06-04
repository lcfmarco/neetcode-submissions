class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Things to store:
            # Result
            # a set of things we have already stored
            # Current list

        curr = []
        record = set()
        res = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:

                if num in record:
                    continue

                curr.append(num)
                record.add(num)
                
                backtrack()

                curr.pop()

                record.remove(num)

            return

        backtrack()

        return res