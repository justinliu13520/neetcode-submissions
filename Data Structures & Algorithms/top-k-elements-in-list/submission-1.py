class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [[],[],[],[]] num with freq
        #   0  1  2  3  Frequency

        freq_dict = dict()
        for n in nums:
            freq_dict[n] = freq_dict.get(n,0) + 1
        freq_list = []
        for j in range(len(nums)+1):
            freq_list.append([])
        for key,val in freq_dict.items():
            freq_list[val].append(key)
        res = []
        for i in range(len(freq_list)-1,-1,-1):
            for r in freq_list[i]:
                res.append(r)
            if len(res) == k:
                return res
