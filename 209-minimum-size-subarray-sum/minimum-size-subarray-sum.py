class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # [1,3,4,6,2] non sorted 
        #target is > 0 
        # return min len of subarray which is >= than target. 
        #if not possible return 0 


        #Pattern: 
        # must be sliding window so we have two pointer starting 0,1 ->, ->[4,2,1,5,,_,_,_]
        # we need to update a min len with min(curr)
        n = len(nums)
        lp = rp = curr_sum = 0
        best = float("inf")

        while True:
            if curr_sum >= target:
                best = min(best, rp-lp)      # window length
                curr_sum -= nums[lp]            # drop the left element
                lp += 1
            elif rp < n:
                curr_sum += nums[rp]            # take the next element
                rp += 1
            else:
                break                      # sum too small and nothing left to add

        return 0 if best == float("inf") else best



        


        
             
