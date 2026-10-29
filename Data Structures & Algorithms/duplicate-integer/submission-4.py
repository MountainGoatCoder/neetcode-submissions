class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        for n in nums:
            if n in hash_table:
                return True
            else:
                hash_table.add(n)
        return False