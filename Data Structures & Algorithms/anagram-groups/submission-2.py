class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = defaultdict(list)

        for s in strs:
            character_counter = [0]*26
            for c in s:
                character_counter[ord(c)-97] += 1
            hash_table[tuple(character_counter)].append(s)
        
        return list(hash_table.values())

                
