class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None: return 

        rows = len(grid)
        cols = len(grid[0])
        visited =  set()
        islands = 0

        def dfs(r,c):
            if( r >= rows or c >= cols or r < 0 or c < 0  or grid[r][c] == "0"  or  (r,c) in visited):
                return
            # check for invalidness
            # already visited
            # is end of dfs
            # out of bounds
            visited.add((r,c))
            
            #explore up, down, left, right
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):   
                if (r,c) not in visited and grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)

        return islands

