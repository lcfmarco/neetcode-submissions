class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}

        for index, num in enumerate(nums):
            difference = target - num
            if target - num not in hash_dict:
                hash_dict[num] = index
            
            else:
                return [hash_dict[difference], index]
        
        return
