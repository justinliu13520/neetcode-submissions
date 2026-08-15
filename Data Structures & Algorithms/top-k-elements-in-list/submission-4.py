class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums)+1)]
        # [[] [] [] [] []]
        #  0  1  2  3  4

        freq_dict = defaultdict(int)

        for n in nums:
            freq_dict[n] += 1

        for num, freq in freq_dict.items():
            freq_list[freq].append(num)

        res = []
        for i in range(len(freq_list)-1,-1,-1):
            for j in freq_list[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res