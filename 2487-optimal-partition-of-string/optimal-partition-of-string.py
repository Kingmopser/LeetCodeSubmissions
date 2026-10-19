class Solution:
    def partitionString(self, s: str) -> int:
        len_sub_string = 1
        curr_set = set()
        for l in s:
            if l not in curr_set:
                curr_set.add(l)
            else:
                len_sub_string +=1
                curr_set = set(l)
        return len_sub_string
