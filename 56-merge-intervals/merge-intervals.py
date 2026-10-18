class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        if len(intervals) <2: 
            return intervals
        intervals.sort()

        merged = list() # stack
        for interval in intervals:
            print(interval)
            if len(merged) ==0:
                merged.append(interval)

            if merged: # start
                curr = merged[-1]
                if interval[1] >=curr[1] and curr[1] >= interval[0]:
                    curr[1] = interval[1]
                    curr[0] = min(interval[0],curr[0])
                    print(merged)
                elif interval[1] == curr[0]:
                    curr[0] = min(interval[0],curr[0])
                    merged.append(interval)
                elif interval[0] >= curr[0] and interval[1] <=curr[1]:
                    continue
                else:
                    merged.append(interval)
                
        
        print(merged)
        return merged 

