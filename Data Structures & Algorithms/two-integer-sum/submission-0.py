class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table = {nums[0]: 0} # constraint: 2 <= nums.length
        
        for i, n in enumerate(nums[1:]): # note that idx = i+1
            if target - n in hash_table:
                return [hash_table[target-n], i+1]
            else:
                hash_table[n] = i+1