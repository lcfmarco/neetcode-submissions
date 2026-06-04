class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n

        postfix = [0] * n

        res = [0] * n

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1 * nums[i] 

            else:
                prefix[i] = nums[i] * prefix[i - 1]

        for x in range(len(nums) - 1, -1, -1):
            if x == len(nums) - 1:
                postfix[x] = 1 * nums[x]
            else:

                postfix[x] = nums[x] * postfix[x + 1]

        for i in range(len(res)):
            if i == 0:
                res[i] = postfix[i + 1]

            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]

            else:
                res[i] = prefix[i - 1] * postfix[i + 1]

        return res
        
        