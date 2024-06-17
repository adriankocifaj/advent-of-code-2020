# problem: https://adventofcode.com/2020/day/11


def read_file(file_name: str, data: list[list[str]]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(list(line.strip()))


def fill_adjacent(data: list[list[str]],
                  dictionary: dict[tuple[int, int], set[tuple[int, int]]],
                  further: bool) -> None:
    rows: int = len(data)
    cols: int = len(data[0])

    def in_bounds(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == ".":
                continue

            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:

                row: int = r + dr
                col: int = c + dc

                if not in_bounds(row, col):
                    continue

                if further:
                    while data[row][col] == ".":
                        row += dr
                        col += dc
                        if not in_bounds(row, col):
                            break

                if not in_bounds(row, col):
                    continue

                if (r, c) not in dictionary:
                    dictionary[(r, c)] = set()
                dictionary[(r, c)].add((row, col))


def adjacent_occupied_counter(data: list[list[str]],
                              dictionary: dict[tuple[int, int], set[tuple[int, int]]],
                              r: int, c: int) -> int:
    if (r, c) not in dictionary.keys():
        return 0

    counter: int = 0
    for row, col in dictionary[(r, c)]:
        if data[row][col] == "#":
            counter += 1
    return counter


def occupied_counter(data: list[list[str]]) -> int:
    counter: int = 0
    rows: int = len(data)
    cols: int = len(data[0])

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "#":
                counter += 1

    return counter


def solution(data: list[list[str]],
             dictionary: dict[tuple[int, int], set[tuple[int, int]]],
             condition: int) -> int:
    rows: int = len(data)
    cols: int = len(data[0])
    change: bool = True
    changes: set[tuple[int, int]] = set()

    while change:
        change = False

        for r in range(rows):
            for c in range(cols):
                if data[r][c] == ".":
                    continue

                occupied: int = adjacent_occupied_counter(data, dictionary, r, c)
                if data[r][c] == "L" and not occupied:
                    changes.add((r, c))
                    change = True
                if data[r][c] == "#" and occupied >= condition:
                    changes.add((r, c))
                    change = True

        for row, col in changes:
            if data[row][col] == "L":
                data[row][col] = "#"
            else:
                data[row][col] = "L"

        changes.clear()

    return occupied_counter(data)


if __name__ == '__main__':
    data: list[list[str]] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)
    adjacent: dict[tuple[int, int], set[tuple[int, int]]] = dict()
    fill_adjacent(data, adjacent, False)

    print(solution(data, adjacent, 4))

    data.clear()
    adjacent.clear()
    read_file(file_name, data)
    fill_adjacent(data, adjacent, True)
    print(solution(data, adjacent, 5))
