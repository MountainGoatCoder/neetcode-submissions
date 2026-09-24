class Solution:

    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        # Runtime: 229ms | Beats 20.78%

        hash_table = defaultdict(list)

        for s in strs:
            character_counter = [0]*26
            for c in s:
                character_counter[ord(c)-97] += 1
            hash_table[tuple(character_counter)].append(s)
        
        return list(hash_table.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = defaultdict(list)

        for s in strs:
            key = frozenset(Counter(s).items())
            hash_table[key].append(s)
        
        return list(hash_table.values())

                
