class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <1:
            return 0
        le=len(s)
        pleft = 0
        pright = 1 if le >1 else 0
        seq = set(s[pleft])
        counter = 1 if le >1 else le
        while (pleft < pright):
            if pright >= le or pleft >= le:
                break
            r = s[pright]
            if r not in seq:
                seq.add(r)
                pright+=1
            elif r in seq:
                pleft +=1
                pright = pleft +1
                counter = max(len(seq),counter)
                seq = set(s[pleft])
            counter = max(len(seq),counter)

        return counter
        
            