class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output_list = []
        cur_state = list(pairs)
        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and cur_state[j].key > cur_state[j + 1].key:
                cur_state[j], cur_state[j + 1] = cur_state[j + 1], cur_state[j]
                j -= 1
            output_list.append(list(cur_state))
        return output_list