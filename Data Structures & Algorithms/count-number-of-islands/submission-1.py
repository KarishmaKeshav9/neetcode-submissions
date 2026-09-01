class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        islands = 0
        visited_set = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited_set.add((r,c))

            while q:
                qrow, qcol = q.popleft()
                directions = [[-1,0], [1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = qrow+dr, qcol+dc
                    if (nr in range(row) and nc in range(col) and grid[nr][nc]=="1" and (nr,nc) not in visited_set):
                        q.append((nr,nc))
                        visited_set.add((nr,nc))



        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited_set:
                    bfs(r,c)
                    islands+=1
        
        return islands
        