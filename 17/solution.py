# problem: https://adventofcode.com/2020/day/17


def read_file(file_name: str, grid: set[tuple[int, int, int]]) -> tuple[int, int]:
    y: int = 0
    z: int = 0
    x: int = 0
    with open(file_name, 'r') as file:
        for line in file:
            x = 0
            for character in line.strip():
                if character == "#":
                    grid.add((x, y, z))
                x += 1
            y += 1

    return x, y


def active_neighbours_counter_3d(grid: set[tuple[int, int, int]], position: tuple[int, int, int]) -> int:
    active: int = 0
    x: int = position[0]
    y: int = position[1]
    z: int = position[2]

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) in grid:
                    active += 1

    if position in grid:
        active -= 1

    return active


def active_neighbours_counter_4d(grid: set[tuple[int, int, int, int]], position: tuple[int, int, int, int]) -> int:
    active: int = 0
    x: int = position[0]
    y: int = position[1]
    z: int = position[2]
    w: int = position[3]

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for m in range(w - 1, w + 2):
                    if (i, j, k, m) in grid:
                        active += 1

    if position in grid:
        active -= 1

    return active


def first_star(grid: set[tuple[int, int, int]], width: int, height: int, depth: int, iterations: int) -> int:
    current_grid: set[tuple[int, int, int]] = grid.copy()
    next_grid: set[tuple[int, int, int]] = set()
    for i in range(1, iterations + 1):
        for x in range(0 - i, width + i):
            for y in range(0 - i, height + i):
                for z in range(0 - i, depth + i):
                    position: tuple[int, int, int] = (x, y, z)
                    active_neighbours: int = active_neighbours_counter_3d(current_grid, position)
                    if ((position in current_grid and (active_neighbours in {2, 3})) or
                            (position not in current_grid and active_neighbours == 3)):
                        next_grid.add(position)
        current_grid = next_grid.copy()
        next_grid.clear()

    return len(current_grid)


def second_star(grid: set[tuple[int, int, int]], width: int, height: int, depth: int, fourth: int,
                iterations: int) -> int:
    current_grid: set[tuple[int, int, int, int]] = set()
    for position in grid:
        current_grid.add((position[0], position[1], position[2], 0))

    next_grid: set[tuple[int, int, int, int]] = set()
    for i in range(1, iterations + 1):
        for x in range(0 - i, width + i):
            for y in range(0 - i, height + i):
                for z in range(0 - i, depth + i):
                    for w in range(0 - i, fourth + i):
                        position: tuple[int, int, int, int] = (x, y, z, w)
                        active_neighbours: int = active_neighbours_counter_4d(current_grid, position)
                        if ((position in current_grid and (active_neighbours in {2, 3})) or
                                (position not in current_grid and active_neighbours == 3)):
                            next_grid.add(position)
        current_grid = next_grid.copy()
        next_grid.clear()

    return len(current_grid)


if __name__ == '__main__':
    grid: set[tuple[int, int, int]] = set()
    file_name: str = "input.txt"
    width, height = read_file(file_name, grid)
    depth: int = 1
    fourth: int = 1
    iterations: int = 6

    print(first_star(grid, width, height, depth, iterations))
    print(second_star(grid, width, height, depth, fourth, iterations))
