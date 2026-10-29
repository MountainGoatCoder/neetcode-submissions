class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = defaultdict(int)
        for char in s:
            hash_table_s[char] += 1
        for char in t:
            if hash_table_s[char] == 0:
                return False
            else:
                hash_table_s[char] -= 1
        for v in hash_table_s.values():
            if v > 0:
                return False
        return True