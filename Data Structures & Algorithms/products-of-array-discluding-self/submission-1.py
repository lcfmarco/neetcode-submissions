class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        suffix = [1] * len(nums)

        res = []
        
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]

            else:
                prefix[i] = nums[i] * prefix[i-1]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix[j] = nums[j]
            else:
                suffix[j] = nums[j] * suffix[j + 1]

        for x in range(len(nums)):
            if x == 0:
                res.append(suffix[x + 1])

            elif x == len(nums) - 1:
                res.append(prefix[x - 1])

            else:
                res.append(suffix[x + 1] * prefix[x - 1])

        return res