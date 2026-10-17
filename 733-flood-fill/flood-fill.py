class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # define dfs and its check then recursion 
        if color == image[sr][sc]: return image
        original_color= image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        def dfs(r,c):
            if (r < 0 or r >=rows or c <0 or c >=cols or image[r][c]!= original_color):
                return
            # already been there, 
            #row and col out of bounds
            # and item same color as image[sr][sc]
            #
            image[r][c] = color
            #explore up, down,left,right
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        dfs(sr,sc) # run dfs once since we only need to do it from one spot, no need to check for n islands

        return image # return image since its modified in place