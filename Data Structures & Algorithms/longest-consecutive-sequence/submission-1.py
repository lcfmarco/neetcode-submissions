class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_hash = set(nums)

        maxlength = 0

        for num in consecutive_hash:
            length = 0

            if num - 1 not in consecutive_hash:
                
                while num in consecutive_hash:
                    length += 1
                    num = num + 1

            maxlength = max(maxlength, length)

        return maxlength

