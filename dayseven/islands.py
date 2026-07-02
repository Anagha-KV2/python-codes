def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'  # mark as visited

        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# User Input
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []
print("Enter the grid row by row (0 or 1):")
for _ in range(m):
    row = input().split()
    grid.append(row)

print("Number of Islands:", numIslands(grid))