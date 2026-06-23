class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash: dict[int, int] = {}
        isDuplicate = False
        
        for num in nums:
            if (num in nums_hash):
                isDuplicate = True
                break
            nums_hash[num] = 1

        return isDuplicate


        