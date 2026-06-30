class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)

        # counts frequency of each number in a hash table
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1
        
        # sorts the dict by values via a lambda that targets the values
        sorted_frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))

        # returns the first k elements
        return list(sorted_frequency_dict)[:k]