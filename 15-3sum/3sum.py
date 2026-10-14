class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        p1 = 0
        p2 = 1
        p3 = l-1
        nums.sort()
        res = set()
        while(p1 < p2 and p1 < p3 and p3 > p2):
            if p1 >=1 and nums[p1-1] == nums[p1]:
                p1+=1
                p2 =p1+1
                p3 = l-1
                continue
            else:
                while (p1 < p2 and p1 < p3 and p3 > p2):
                    curr = nums[p2] + nums[p3]
                    target = nums[p1] * (-1)
                    trip = tuple([nums[p1],nums[p2],nums[p3]])
                    if curr < target:
                        p2+=1
                    elif curr > target:
                        p3-=1
                    elif curr == target:
                        res.add(trip)
                        p2+=1
                        continue
                    else:
                        break
            p1+=1
            p2 =p1+1
            p3 = l-1
        return [list(k) for k in list(res)]

