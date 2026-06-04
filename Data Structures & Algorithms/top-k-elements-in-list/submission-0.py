class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        for num, cnt in num_dict.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                
                res.append(c)
                
                if len(res) == k:
                    return res
                

        