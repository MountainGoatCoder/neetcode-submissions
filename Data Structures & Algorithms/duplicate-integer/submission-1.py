class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for n in nums:
            if n in hash_table:
                return True
            else:
                hash_table[n] = 1
        return False