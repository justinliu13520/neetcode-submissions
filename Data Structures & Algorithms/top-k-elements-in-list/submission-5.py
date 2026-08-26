class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums) + 1)]
        freq_dict = defaultdict(int)
        for n in nums:
            freq_dict[n] += 1
        
        for key,value in freq_dict.items():
            freq_list[value].append(key)
        # print(freq_list)
        res = []
        for i in range(len(freq_list)-1,-1,-1):
            for element in freq_list[i]:
                if len(res) == k:
                    return res
                res.append(element)
        return res
