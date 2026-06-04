class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_i = 0
        sol_j = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
