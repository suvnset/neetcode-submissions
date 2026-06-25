class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for index, num in enumerate(nums):
            if num not in nums_hash:
                nums_hash[num] = []
            nums_hash[num].append(index)
            
            diff = target - num
            if (diff in nums_hash):
                if (num != diff):
                    return sorted([nums_hash[num][0], nums_hash[diff][0]])
                elif len(nums_hash[num]) > 1:
                    return sorted([nums_hash[num][0], nums_hash[num][1]])