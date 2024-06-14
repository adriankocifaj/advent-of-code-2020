# problem: https://adventofcode.com/2020/day/3


def read_file(file_name: str, data: list[str]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())


def first_star(data: list[str], slope: tuple[int, int]) -> int:
    counter: int = 0
    position: list[int] = [0, 0]
    rows: int = len(data)
    cols: int = len(data[0])

    while True:
        if data[position[0]][position[1]] == "#":
            counter += 1

        position[0] += slope[0]
        position[1] = (position[1] + slope[1]) % cols

        if position[0] >= rows:
            break

    return counter


def second_star(data: list[str], slopes: list[tuple[int, int]]) -> int:
    result: int = 1

    for slope in slopes:
        result *= first_star(data, slope)

    return result


if __name__ == '__main__':
    data: list[str] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)
    slope: tuple[int, int] = (1, 3)
    slopes: list[tuple[int, int]] = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    print(first_star(data, slope))
    print(second_star(data, slopes))
