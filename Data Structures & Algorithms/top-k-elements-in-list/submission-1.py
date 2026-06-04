class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, make a dictionary with all the frequencies
        # Second, form a frequency list, in which each index is the count
            # We will use this frequency to traverse down

        freq_dict = {}

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        for num, cnt in freq_dict.items():
            freq[cnt].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)

                if len(res) == k:
                    return res

        