class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}

        for num in range(len(nums)):
            diff = target - nums[num]

            if diff in diff_dict:
                return [diff_dict[diff], num]
        
            diff_dict[nums[num]] = num

        