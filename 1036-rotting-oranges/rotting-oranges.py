class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # quick check 
        # init vars 
        # append starting elem to queue 
        # add as visiited 
        # loop in 4 dirctions
        # new r,c and then check the conditions also if == 0
        # make changes 
        # we need to iter from each rotten orange to determine the min number of minutes (iterations) unti all become rotten. 
        cols = len(grid[0])
        rows =len(grid)
        visited = set()
        queue = deque()
        fresh_oranges = 0
        max_minutes = 0
        if rows <1 or cols > 10:
            return 
        # iter thorugh all r, and c where orange == rotten. 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges+=1
                elif grid[r][c] == 0:
                    continue
                else:
                    queue.append((r,c,0))
                    visited.add((r,c))

        if fresh_oranges==0: return 0
        minutes =0
        while queue:
            r,c,m= queue.popleft()
            max_minutes=max(max_minutes,m)
            m +=1   
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                newr,newc = r + dr, c+ dc
                if newr < 0 or newr >= rows or newc < 0 or newc >= cols or (newr,newc) in visited or grid[newr][newc] == 0:
                    continue
                grid[newr][newc] = 2
                fresh_oranges -=1
                queue.append((newr,newc,m))
                visited.add((newr,newc))

        if fresh_oranges  == 0:
            return max_minutes
        return -1

