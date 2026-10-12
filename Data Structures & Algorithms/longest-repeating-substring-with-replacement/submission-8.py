class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = len(s)
        if l <= k+1:
            return l

        frequency = [0]*26

        max_f = 0

        w_start = 0
        w_end = 0

        max_len = k+1

        while w_end < l and w_start <= w_end:

            c = ord( s[w_end] ) - 75
            frequency[c] += 1

            if max_f < frequency[c]:
                max_f = frequency[c]

            # len of current substring: window_end - window_start + 1
            if w_end - w_start + 1 - max_f <= k: # window is valid, update and increase
                max_len = max(max_len, w_end - w_start + 1)
                w_end += 1
            else: # not valid, slide it
                frequency[ ord( s[w_start] ) - 75 ] -= 1
                max_f = max(frequency) # can be optimized
                w_start = w_start+1
                w_end = w_end+1
        
        return max_len

    def characterReplacement_v1(self, s: str, k: int) -> int:

        l = len(s)
        if l <= k+1:
            return l

        # char_pos[idx(c)] = [
        #   [
        #       start_pos, 
        #       window_len, 
        #       number_occurences_in_window
        #   ], ...
        # ]
        char_pos = [[] for i in range(26)]
        max_window_len = k

        for i, c in enumerate(s):
            idx_c = ord(c) - 75
            for j in range( len( char_pos[idx_c] ) ):
                # it is valid to extend the window
                if i - char_pos[idx_c][j][0] - 1 - char_pos[idx_c][j][2] <= k:
                    char_pos[idx_c][j][2] += 1
                    char_pos[idx_c][j][1] = min( 
                        k + char_pos[idx_c][j][2], 
                        l-1
                    )
                    
                    if char_pos[idx_c][j][1] > max_window_len:
                        max_window_len = char_pos[idx_c][j][1]
                # window cannot be extended further (complicates indexing)
                # else: 
                #     if char_pos[idx_c][j][1] < max_window_len:
                #         del char_pos[idx_c][j]

            # initiate new window
            char_pos[idx_c].append( [i, min(k, l-i-1), 0] )
        
        return max_window_len + 1 # plus 1 to include first character
