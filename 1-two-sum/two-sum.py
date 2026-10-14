class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        seen =  dict()
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in seen:
                return [seen.get(diff), n]
            seen[nums[n]]=n
            

