class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]
        row, col = len(image), len(image[0])

        def dfs(r, c):
            if r in range(row) and c in range(col) and image[r][c] == cur_color and image[r][c] != color:
                image[r][c] = color
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r, c-1)
                dfs(r, c+1)
        
        dfs(sr, sc)
        return image
        