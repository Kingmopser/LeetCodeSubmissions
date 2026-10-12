class Solution:
    def maxArea(self, height: list[int]) -> int:
        def area(p1,p2):
            a = p2 - p1 
            b = min(height[p1],height[p2])
            U = a * b
            return U

        U = list()
        l = len(height)
        p1 = 0
        p2 = l - 1
        while p1 < p2:
            U.append(area(p1,p2))
            if height[p1]< height[p2]:
                p1+=1
            elif height[p1]> height[p2]:
                p2-=1
            elif height[p1]== height[p2]:
                p2-=1
        return max(U)



