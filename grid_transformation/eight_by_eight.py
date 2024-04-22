def rotate_grid_90_clockwise(grid):
    n = len(grid)  # Assuming the grid is square and its length is 8
    # Create a new grid of the same size, initializing with zeroes or similar values
    new_grid = [[0] * n for _ in range(n)]

    # Fill in the new grid based on the rotation
    for x in range(n):
        for y in range(n):
            new_grid[y][n - 1 - x] = grid[x][y]

    return new_grid


def rotate_grid_90_counterclockwise(grid):
    n = len(grid)  # Assuming the grid is square and its length is 8
    # Create a new grid of the same size, initializing with zeroes or similar values
    new_grid = [[0] * n for _ in range(n)]

    # Fill in the new grid based on the rotation
    for x in range(n):
        for y in range(n):
            new_grid[n - 1 - y][x] = grid[x][y]

    return new_grid


# Example usage:
original_grid = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64],
]

print("Original Grid:")
for row in original_grid:
    print(row)

print("\nRotated Grid (90 degrees clockwise):")
rotated_grid = rotate_grid_90_clockwise(original_grid)
for row in rotated_grid:
    print(row)

print("\nRotated Grid (90 degrees counterclockwise):")
rotated_grid = rotate_grid_90_counterclockwise(original_grid)
for row in rotated_grid:
    print(row)
