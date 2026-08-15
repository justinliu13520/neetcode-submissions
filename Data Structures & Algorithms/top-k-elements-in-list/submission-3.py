class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        freq_list = [[] for _ in range(len(nums)+1)]

        for n in nums:
            freq_dict[n] += 1
        
        for num, freq in freq_dict.items():
            freq_list[freq].append(num)
            
        output_list = []
        for i in range(len(freq_list)-1,-1,-1):
            for j in freq_list[i]:
                output_list.append(j)
                if len(output_list) == k:
                    return output_list
        return output_list