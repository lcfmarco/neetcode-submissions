class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_hash = set(nums)
        if len(num_hash) < len(nums):
            return True
        else:
            return False
