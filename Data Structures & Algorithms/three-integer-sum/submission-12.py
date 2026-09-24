class Solution:
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: O(n^3)
        t_dict = {}
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = tuple(sorted([nums[i],nums[j],nums[k]]))
                        t_dict[t] = True
        return [list(k) for k in t_dict.keys()]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(nums)
        triplets = []
        prev_nums_i = -10**5-1
        for i in range(n-2):
            if sorted_nums[i] == prev_nums_i:
                continue
            print(f"\n i: {i} -- ", end="")
            target = -sorted_nums[i]
            j = i+1
            k = n-1
            while j<k:
                if sorted_nums[j] + sorted_nums[k] > target:
                    k = k-1
                elif sorted_nums[j] + sorted_nums[k] < target:
                    j = j+1
                else:
                    triplets.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    # avoid duplicates
                    new_j = j+1
                    while new_j <= n-1 and sorted_nums[j] == sorted_nums[new_j]:
                        new_j = new_j+1
                    j = new_j
                    k = k-1
            prev_nums_i = sorted_nums[i]

        return triplets