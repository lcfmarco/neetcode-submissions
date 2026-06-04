class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_dict = {}

        for n in range(len(nums)):
            difference = target - nums[n]

            if difference in difference_dict:
                return [difference_dict[difference], n]
            difference_dict[nums[n]] = n
        
