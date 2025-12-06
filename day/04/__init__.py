def part1(input):
    return len(_removable(input))


def part2(input):
    input = [list(row) for row in input]

    total_removed = 0
    removed = _remove_possible(input)

    while removed:
        total_removed += removed
        removed = _remove_possible(input)

    return total_removed


def _remove_possible(input):
    removed = _removable(input)

    for x, y in removed:
        input[x][y] = "."

    return len(removed)


def _removable(input):
    removable = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] != ".":
                neighbors = [n for n in _get_neighbors(input, x, y) if n != "."]
                if len(neighbors) < 4:
                    removable.append((x, y))
    return removable


def _get_neighbors(grid, x, y):
    neighbors = []
    for dx, dy in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, -1),
        (1, 1),
    ]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append(grid[nx][ny])

    return neighbors
