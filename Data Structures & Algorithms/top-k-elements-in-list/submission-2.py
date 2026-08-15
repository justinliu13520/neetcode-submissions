class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums)+1)]
        freq_dict = {}
        
        for n in nums:
            freq_dict[n] = freq_dict.get(n,0) + 1
        print(freq_dict)
        for num,freq in freq_dict.items():
            freq_list[freq].append(num)
        output_list = []
        for i in range(len(nums),-1,-1):
            for j in range(len(freq_list[i])):
                output_list.append(freq_list[i][j])
                if len(output_list) == k:
                    return output_list
        return []