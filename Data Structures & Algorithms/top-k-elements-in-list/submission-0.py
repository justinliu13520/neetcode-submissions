class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        sorted_items = sorted(freq_dict.items(), key=lambda item: item[1])

        last_x_keys = [item[0] for item in sorted_items[-k:]]
        return last_x_keys