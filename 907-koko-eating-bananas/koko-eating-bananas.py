class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #array len n 
        # k = bananas/hour
        # each hour she eats k banas 
        # if piles[i] <k , she finished all and needs 1hours
        # min k so that sum(piles)/k < h
        # 3 -> 1hours
        # 6 -> 2 hours 
        # 7 -> 2 hours
        # 11 -> 2 hours
        # binary search on the answer space k
        l = 1
        upper = max(piles)
        
        min_time = 0
        def hours_needed(k):
            time_needed = 0 
            for n in piles:
                time_needed += (n + k - 1) // k

            return time_needed
        
        #perform binary search
        u = upper
        res = 0
        while l <= u:
            curr=  l+ (u -l) // 2

            if hours_needed(curr) > h:
                l = curr +1

            elif hours_needed(curr)<=h:
                res = curr
                u = curr-1
                #good

        return res
        

        