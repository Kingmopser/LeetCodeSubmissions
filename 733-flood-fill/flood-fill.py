from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        if color == image[sr][sc]: return image

        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])

        while queue:
            r,c = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_r,new_c = r+ dr , c + dc    
                if new_r >= rows or new_r<0 or new_c >= cols or new_c <0 or image[new_r][new_c] != original_color:
                    continue
                image[new_r][new_c] = color
                visited.add((new_r, new_c))
                queue.append((new_r, new_c))
            
                
        return image # return image since its modified in place