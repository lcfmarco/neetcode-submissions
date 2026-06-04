class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
            else:
                return True
        return False